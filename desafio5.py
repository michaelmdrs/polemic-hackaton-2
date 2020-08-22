"""
Desafio 5 - Verificar password
"""
import random
from time import sleep

password = input('Digite uma senha: ')

if len(password) < 6:
    print('Senha, FRACA!')
elif len(password) >= 6 and len(password) <= 12:
    print('Senha, MÉDIA!')
else:
    print('Senha, FORTE!')