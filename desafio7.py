"""
Desafio 7 - Formatando número de telefone
"""
numero_telefone = input('Digite um número de telefone: ')

if len(numero_telefone) != 11:
    raise ValueError
else:
    numero_telefone = int(numero_telefone)
    numero_telefone = str(numero_telefone)
    telefone = numero_telefone
    numero_formatado = f'({}) {}.{}-{}' #continua a partir daqui