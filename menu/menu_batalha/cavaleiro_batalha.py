import os
import random

def batalha_cavaleiro(usuario, bot):
    inicio = True  

    while True:
        if inicio:
            print('so aparece 1 vez')
            inicio = False  
        else:
            ataque_bot = random.randint(1,5)
            if ataque_bot in [1, 2, 3]:
                print('Seu inimigo usou: ')
                bot.ataque_basico()
                print('===================\n')
            elif ataque_bot == 4:
                print('Seu inimigo usou: ')
                bot.ataque_pesado()
                print('===================\n')
            elif ataque_bot == 5:
                print('Seu inimigo usou: ')
                bot.ultimate()
                print('===================\n')

        menu_batalha_cavaleiro = input(f'''
Sua vida:{usuario.vida}            Vida do oponente:{bot.vida}           

======= ATAQUES ======
[a] Ataque básico
[s] Ataque pesado
[d] Levantar escudo
[f] Ultimate
======================
Sua escolha: ''')

        os.system('cls')

        if menu_batalha_cavaleiro.lower() == 'a':
            print('você usou:')
            usuario.ataque_basico()
            print('===================\n')
        elif menu_batalha_cavaleiro.lower() == 's':
            print('você usou:')
            usuario.ataque_pesado()
            print('===================\n')
        elif menu_batalha_cavaleiro.lower() == 'd':
            print('você usou:')
            usuario.escudo()
            print('===================\n')
        elif menu_batalha_cavaleiro.lower() == 'f':
            print('você usou:')
            usuario.ultimate()
            print('===================\n')
        else:
            print('Opção inválida!')
