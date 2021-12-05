from coin_system.models import Aluno, Transacao, Vantagem

def get_transaction_history(subject):
  subject_type = type(subject).__name__
  
  kwargs = {subject_type.lower(): subject}
  return Transacao.objects.filter(**kwargs).order_by('-date')


def get_coin_transfer_context(user, updated):
  if hasattr(user, 'professor'):
    related_obj = user.professor
    aluno_list = Aluno.objects.filter(instituicao_ensino=user.professor.instituicao_ensino).order_by('nome')
    vantagem_list = []
  elif hasattr(user, 'aluno'):
    related_obj = user.aluno
    aluno_list = []
    vantagem_list = Vantagem.objects.all().order_by('nome', 'valor')
  else:
    return None

  return {
    'saldo': related_obj.saldo,
    'aluno_list': aluno_list,
    'vantagem_list': vantagem_list,
    'transaction_list': get_transaction_history(related_obj),
    'updated': updated
  }


def process_coin_transfer(user, payload):
  target_aluno = Aluno.objects.get(pk=payload['aluno'])
  exchange_val = max(0, int(payload['value']))
  user.professor.saldo -= exchange_val
  target_aluno.saldo += exchange_val

  user.professor.save()
  target_aluno.save()

  n_t = Transacao(
    professor = user.professor,
    aluno = target_aluno,
    valor = max(0, int(payload['value']))
  )
  n_t.save()


def process_coin_exchange(user, payload):
  aluno = user.aluno
  vantagem = Vantagem.objects.get(pk=payload['vantagem'])

  if aluno.saldo < vantagem.valor:
    return {
      'error': True,
      'message': 'Você não possui saldo suficiente para esta transação'
    }
  else:
    n_t = Transacao(
      vantagem = vantagem,
      aluno = aluno,
      valor = vantagem.valor
    )
    aluno.saldo -= vantagem.valor

    n_t.save()
    aluno.save()
    return {
      'error': False,
      'message': '',
      'confirmation': n_t.id
    }

