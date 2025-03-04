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
            usuario = cavaleiro(vida=150, forca=15, estamina=4, defesa=10, status_defesa=False)
            os.system('cls')
            print('cavaleiro criado!')
            return usuario
        
        elif escolha.lower() == 'm':
           usuario =  mago(vida=100 , mana=50, forca=40, poder=10)
           os.system('cls')
           print('Mago criado!')
           return usuario
        else:
            os.system('cls')
            print('Opção inválida!')