import os


def menu_principal():
    while True:
        menu_principal = input('''
XXXXXXXX Menu Principal XXXXXXXXXX
[a] Iniciar batalha
[s] Trocar o personagem
[d] Criar personagem novo
[f] Ver seus personagens
[q] Sair do progama
XXXXXXXX                XXXXXXXXXX
Sua escolha:''')
    
        if menu_principal.lower() == 'a':
            os.system('cls')
            print('Batalha iniciando...')
            return 
        elif menu_principal.lower() == 's':
            os.system('cls')
            print('ainda nao esta pronto')
            return 
        else:
            os.system('cls')
            print('ainda em desenvolvimento')
            return