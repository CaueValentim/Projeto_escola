import os
# Projeto para calcular a media dos alunos de uma escola.

# Nesse projeto, os alunos que quiserem saber se serão aprovados
# digirarão suas medias e será feito o calculo automatico para eles.

# passo 1: Criação das variaveis e solicitar a entrada de dados.

Nota1 = int(input('Digite sua nota: '))
Nota2 = int(input('Digite sua nota: '))
Nota3 = int(input('Digite sua nota: '))
Nota4 = int(input('Digite sua nota: '))

media = (Nota1 + Nota2 + Nota3 + Nota4) / 4


if media < 6:
    {
        print(f'Sua media é: {media}, então você está REPROVADO')
    }
else:
    print(f'Sua media é: {media}, então você está APROVADO')


os.system('pause')
