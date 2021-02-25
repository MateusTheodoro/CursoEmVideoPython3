dia = int(input('Quantos dias foram rodados: '))
km = float(input('Quantos KM foram rodados: '))
pago = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
