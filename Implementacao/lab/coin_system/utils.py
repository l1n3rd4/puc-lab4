from coin_system.models import Aluno

def get_coin_transfer_context(user, updated):
  if hasattr(user, 'professor'):
    related_obj = user.professor
    aluno_list = Aluno.objects.filter(instituicao_ensino=user.professor.instituicao_ensino).order_by('nome')
  elif hasattr(user, 'aluno'):
    related_obj = user.aluno
    aluno_list = []
  else:
    return None

  return {
    'saldo': related_obj.saldo,
    'aluno_list': aluno_list,
    'updated': updated
  }

def process_coin_transfer(user, payload):
  target_aluno = Aluno.objects.get(pk=payload['aluno'])
  exchange_val = max(0, int(payload['value']))
  user.professor.saldo -= exchange_val
  target_aluno.saldo += exchange_val

  user.professor.save()
  target_aluno.save()
