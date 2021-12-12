from coin_system.models import Aluno, Transacao, Vantagem, Empresa
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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


def register_user(payload, registration_type):
  if User.objects.filter(username=payload['user']).exists():
    return {
      'error': 'Usuário já existe'
    }
  
  new_user = User(
    username = payload['user'],
    first_name = payload['nome'],
    email = payload['email'],
    password = make_password(payload['password']),
    is_active = True
  )
  new_user.save()

  if registration_type == 'aluno':
    new_object = Aluno(
      user = new_user,
      nome = payload['nome'],
      email = payload['email'],
      cpf = payload['cpf'],
      rg = payload['rg'],
      endereco = payload['endereco'],
      instituicao_ensino = payload['instituicao'],
      curso = payload['curso']
    )
  else:
    new_object = Empresa(
      user = new_user,
      nome = payload['nome']
    )
  new_object.save()

  return {
    'success': True
  }


def create_empresa_vantagem(payload, empresa):
  new_vant = Vantagem(
    nome = payload['nome'],
    descricao = payload['descricao'],
    valor = int(payload['valor']),
    empresa = empresa
  )
  new_vant.save()
  return {
    'created': True
  }
