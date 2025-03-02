from classes.mago import mago
from classes.cavaleiro import cavaleiro
import os


usuario = cavaleiro(vida=150, forca=15,estamina=4, defesa=10, status_defesa=False)

usuario.ataque_pesado()
usuario.escudo()
usuario.recebendo_dano(8)
usuario.recebendo_dano(12)

while True:
    menu_personagem = input(''' 
XXXXXX Escolha Sua Classe XXXXXX
[c] Cavaleiro
[m] Mago
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Sua escolha: ''')
    
    if menu_personagem.lower() == 'c':
        usuario = cavaleiro(vida=150, forca=15, estamina=4, defesa=10, status_defesa=False)
        os.system('cls')
        print('cavaleiro criado!')
        break
        
    elif menu_personagem.lower() == 'm':
        usuario =  mago(vida=100 , mana=50, forca=40, poder=10)
        os.system('cls')
        print('Mago criado!')
        break

while True:
    menu_batalha_cavaleiro = input('''
======= BATALHA ======
[a] Ataque básico
[s] Ataque pesado
[d] Levantar escudo
[f] Ultimate
======================
Sua escolha: ''')
    
    if menu_batalha_cavaleiro.lower() == 'a':
        os.system('cls')
        usuario.ataque_basico()
    elif menu_batalha_cavaleiro.lower() == 's':
        os.system('cls')
        usuario.ataque_pesado()
    elif menu_batalha_cavaleiro.lower() == 'd':
        os.system('cls')
        usuario.escudo()
    elif menu_batalha_cavaleiro() == 'f':
        os.system('cls')
        usuario.ultimate()