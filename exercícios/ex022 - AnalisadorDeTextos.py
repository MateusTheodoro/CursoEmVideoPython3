nome = str(input('Digite seu nome completo: ')).strip()

maiusc = nome.upper()
print(f'Upper: {maiusc}')

minusc = nome.lower()
print(f'Lower: {minusc}')

print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')

cadaPalavra = nome.split()
print(f'A primeira palavra tem {len(cadaPalavra[0])} letras e a segunda palavra tem {len(cadaPalavra[1])} letras')
