nome = str(input('Digite seu nome completo: '))

maiusc = nome.upper()
print(f'Upper: {maiusc}')

minusc = nome.lower()
print(f'Lower: {minusc}')

semEspaço = nome.replace(' ','')
print(f'Existem {len(semEspaço)} caracteres sem contar os espaços!')

cadaPalavra = nome.split()
print(f'A primeira palavra tem {len(cadaPalavra[0])} letras e a segunda palavra tem {len(cadaPalavra[1])} letras')
