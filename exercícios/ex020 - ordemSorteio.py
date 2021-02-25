from random import shuffle
alunoUm = str(input('Aluno um: '))
alunoDois = str(input('Aluno dois: '))
alunoTres = str(input('Aluno três: '))
alunoQuatro = str(input('Aluno quatro: '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
shuffle(lista)
print(f'Os alunos foram sorteados na ordem: {lista}')
