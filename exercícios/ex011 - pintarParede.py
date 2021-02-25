largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
totalTinta = area / 2
print(f'Sua parede tem a dimensão de (LXA) {largura} x {altura}\n'
      f'E a área total é de {area}m²\n'
      f'A quantidade de tinta será de: {totalTinta:.2f} litros.')
