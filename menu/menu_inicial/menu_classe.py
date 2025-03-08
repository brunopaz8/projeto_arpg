from classes.mago import mago
from classes.cavaleiro import cavaleiro
import os

def escolha_classe():
    while True:
        
        escolha = input(''' 
XXXXXX Escolha Sua Classe XXXXXX
[c] Cavaleiro
[m] Mago
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Sua escolha: ''')
    
        if escolha.lower() == 'c':
            os.system('cls')
            print('Criando um cavaleiro!')
            return escolha
        
        elif escolha.lower() == 'm':
           os.system('cls')
           print('Criando um mago!')
           return escolha
        else:
            os.system('cls')
            print('Opção inválida!')