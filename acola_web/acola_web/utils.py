'''
FUNÇÕES UTILITÁRIAS DO SISTEMA
'''

from acola_web.settings import SECRET_KEY
from hashlib import md5

def converter_senha(senha):
    '''
    Converte a senha para o modelo MD5
    '''
    return md5(str(senha+SECRET_KEY).encode('ascii')).hexdigest()