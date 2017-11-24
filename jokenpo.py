# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:41:07 2017

@author: Leonardo Venancio
"""
from random import randint
from time import sleep

print "\nJO KEN PO!\n"

opcoes = ('Pedra','Papel','Tesoura')

computador = randint(0,2)

#print ('O computador escolheu {}'.format(opcoes[computador]))

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('\nQual sua jogada? '))

print 'JO'
sleep(1)
print 'KEN'
sleep(1)
print 'PO!!'

print('-='*12) 
print('Jogador jogou {}'.format(opcoes[jogador]))
print('Computador jogou {}'.format(opcoes[computador]))
print('-='*12)
if computador == 0:
    if(jogador == 0):
        print "\nEmpate!!"
    elif(jogador == 1):
        print "\nJogador Venceu!!"
    elif(jogador == 2):
        print "\nComputador Venceu!!"
        
elif computador == 1:
    if(jogador == 0):
        print "\nComputador Venceu!!"
    elif(jogador == 1):
        print "\nEmpate!!"
    elif(jogador == 2):
        print "\nJogador Venceu!!"
    
elif computador == 2: 
    if(jogador == 0):
        print "\nJogador Venceu!!"
    elif(jogador == 1):
        print "\nComputador Venceu!!"
    elif(jogador == 2):
        print "\nEmpate!!"



