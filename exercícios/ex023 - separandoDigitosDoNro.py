numero = str(input('Digite um número de 0 a 9999: '))

numeroDiv = numero.split()

print(f'Unidade: {len(numeroDiv[0])}')
print(f'Dezena: {len(numeroDiv[1])}')
print(f'Centena: {len(numeroDiv[2])}')
print(f'Milhar: {len(numeroDiv[3])}')
