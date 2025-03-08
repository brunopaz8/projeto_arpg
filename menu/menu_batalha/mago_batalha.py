import os
import random

def batalha_mago(usuario, bot):
    inicio = True  

    while True:
        if inicio:
            inicio = False  
        else:
            ataque_bot = random.randint(1,6)
            if ataque_bot in [1, 2, 3]:
                print('Seu inimigo usou: ')
                usuario.recebeu_dano(bot.ataque_basico())
                print('===================\n')
            
            elif ataque_bot == 4:
                print('Seu inimigo usou: ')
                usuario.recebeu_dano(bot.ataque_pesado()) 
                print('===================\n')

            elif ataque_bot == 5:
                print('Seu inimigo usou: ')
                bot.habilidade()
                print('===================\n')
            
            elif ataque_bot == 6:
                print('Seu inimigo usou: ')
                usuario.recebeu_dano(bot.ultimate())
                print('===================\n')

        menu_batalha = input(f'''
Sua vida:{usuario.vida}            Vida do oponente:{bot.vida}   
Mana:{usuario.mana}        

======= ATAQUES ======
[a] Bola de fogo
[s] Meteoro
[d] Auto-cura
[f] Chuva de meteoro
======================
Sua escolha: ''')

        os.system('cls')

        if menu_batalha.lower() == 'a':
            print('você usou:')  
            bot.recebeu_dano(usuario.ataque_basico())
            print('===================\n')
        
        elif menu_batalha.lower() == 's':
            print('você usou:')
            bot.recebeu_dano(usuario.ataque_pesado())
            print('===================\n')
       
        elif menu_batalha.lower() == 'd':
            print('você usou:')
            usuario.habilidade()
            print('===================\n')
       
        elif menu_batalha.lower() == 'f':
            print('você usou:')
            bot.recebeu_dano(usuario.ultimate())
            print('===================\n')
       
        else:
            print('Opção inválida!')

        if usuario.vida == 0:
            os.system('cls')
            print('Você perdeu! :(')
            break
        
        elif bot.vida == 0:
            os.system('cls')
            print('Você ganhou! :)')
            break
