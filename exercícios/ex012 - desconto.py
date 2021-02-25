produto = float(input('Digite o preço do produto R$'))
desconto = (produto * 15 / 100)
produtoDesconto = produto - desconto
juros = (produto * 5 / 100)
produtoJuros = juros + produto
print(f'Se pagar à vista')
print(f'O desconto será de R${desconto:.2f}\nE o novo preço do produto é: R${produtoDesconto:.2f}')
print(f'Se pagar à prazo')
print(f'Terá um juros de 5%, que será de R${juros:.2f} e o preço será de R${produtoJuros:.2f}')