from classes.mago import mago
from classes.cavaleiro import cavaleiro

from menu.menu_inicial.menu_classe import escolha_classe
from menu.menu_inicial.menu_principal import menu_principal
import os
import random


usuario = escolha_classe()

menu_principal()


while True:
    
    bot = mago(vida=100 , mana=50, forca=40, poder=10)
    ataque_bot = random.randint(1,5)
    
    if ataque_bot == 1 or ataque_bot == 2 or ataque_bot == 3:
        bot.ataque_basico()
    elif ataque_bot == 4:
        bot.ataque_pesado()
    elif ataque_bot == 5:
        bot.ultimate()
    
    menu_batalha_cavaleiro = input(f'''
  Sua vida:{usuario.vida}            Vida do oponente:{bot.vida}             
                                   
    ======= ATAQUES ======
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
    elif menu_batalha_cavaleiro.lower() == 'f':
        os.system('cls')
        usuario.ultimate()
    else:
        os.system('cls')
        print('Opção inválida!')
