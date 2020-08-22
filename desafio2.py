"""
Desafio 2 - Conversor de Real para centavos - Vice versa
"""
print('-=' * 10)
print('CONVESOR DE MOEDAS')
print('-=' * 10)

vlr_centavos = int(input('Digite o valor em centavos R$: '))
vlr_reais = float(input('Digite o valor em reais R$: '))

centavos = 100
real = 100
conversor_moedas = vlr_centavos / centavos
conversor_reais = vlr_reais * real

print(f'O valor de {vlr_centavos} centavos, convertido em reais é R$ {conversor_moedas}')
print(f'O valor de R$ {vlr_reais:.1f} convertido, em centavos é {conversor_reais:.0f} centavos.')





