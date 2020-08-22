"""
Desafio 1 - Faça um validador de cartões de créditos

"""
numero_cartao = input('Digite o número do cartão: ')

if len(numero_cartao) < 16:
    print('Cartão inválido, insira o número do cartão.')
else:
    print('Cartão validado com sucesso.')