from random import choice
alunoUm = str(input('Digite o nome do aluno um: '))
alunoDois = str(input('Digite o nome do aluno dois: '))
alunoTres = str(input('Digite o nome do aluno três: '))
alunoQuatro = str(input('Digite o nome do aluno quatro: '))
alunos = [alunoUm, alunoDois, alunoTres, alunoQuatro]
print(f'O aluno sorteado para apagar a lousa: {choice(alunos)}')
