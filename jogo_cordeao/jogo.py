from funcoes import *

print('Paciência Acordeão')
print('\n==================\n') 

print('\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n') 

print('\nExistem apenas dois movimentos possíveis:\n') 

print('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print('2. Empilhar uma carta sobre a terceira carta anterior.') 

print('\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n') 

print('1. As duas cartas possuem o mesmo valor ou') 
print('2. As duas cartas possuem o mesmo naipe.\n') 

input('\n Pressione [ENTER] para inciar')

#JOGO


    
import random

continua = True
while continua:
    i = 52
    baralho = cria_baralho()
    random.shuffle(baralho)
    while possui_movimentos_possiveis(baralho):
        for carta in baralho:
            print('{}. {}'.format(baralho.index(carta)+1, carta))
        q = int(input('Digite o número da carta que você escolheu entre 1 e {}:'.format(i)))
        if q <= i:
            if lista_movimentos_possiveis(baralho, q-1)!=[]:
                if lista_movimentos_possiveis(baralho, q-1) == [3]:
                    empilha(baralho, q-1, q-4)
                    i-=1   
                elif lista_movimentos_possiveis(baralho, q-1) == [1]:
                    empilha(baralho, q-1, q-2)
                    i-=1
                elif lista_movimentos_possiveis(baralho, q-1) == [1, 3]:
                    t = True
                    while t:
                        q2 = int(input('Sobre qual carta você quer empilhar o {}?: \n 1.{} \n 2.{}\n'.format(baralho[q-1], baralho[q-2], baralho[q-4])))
                        if q2 == 1:
                            empilha(baralho, q-1, q-2)
                            i-=1
                            t = False
                        elif q2 == 2:
                            empilha(baralho, q-1, q-4)
                            i-=1
                            t = False
                        else:
                            print('Escolha 1 ou 2!')
                            t = True
            else:
                print('A carta {} não pode ser empilhada!'.format(baralho[q-1]))
        else:
            print('Digite um número entre 1 e {}'.format(i))
    if len(baralho)==1:
        print('Você venceu!')
        question = input('Quer jogar de novo?(sim ou não)')
        if question == 'sim':
            continua = True
        else:
            continua = False
    else:
        print('Você perdeu!')
        question = input('Quer jogar de novo?(sim ou não)')
        if question == 'sim':
            continua = True
        else:
            continua = False