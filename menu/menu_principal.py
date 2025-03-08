import os
from menu.menu_inicial.menu_ver_personagem import Ver_personagem

def menu_principal(usuario, escolha):
    while True:
        menu_principal = input('''
XXXXXXXX Menu Principal XXXXXXXXXX
[a] Iniciar batalha
[s] Ver personagem
[d] Trocar personagem
[f] Sair do progama
XXXXXXXX                XXXXXXXXXX
Sua escolha:''')
    
        if menu_principal.lower() == 'a':
            os.system('cls')
            return
        elif menu_principal.lower() == 's':
            os.system('cls')
            Ver_personagem(usuario= usuario, escolha= escolha)
             
        else:
            os.system('cls')
            print('ainda em desenvolvimento')
            