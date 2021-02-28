cidade = str(input('Digite o nome da cidade: '))
maiusc = cidade.upper() #transformando a frase em maiúscula
dividindo = maiusc.split() #dividindo a frase que foi convertida em maiúscula
procurando = 'SANTO' in dividindo[0] #procurando 'SANTO' na primeira palavra da frase

print(f'A cidade {maiusc} começa com "SANTO"?\n"True" para verdadeiro. "False" para falso\n{procurando}')
