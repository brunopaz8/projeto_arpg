import os

os.system('cls')

def Ver_personagem(usuario, escolha):
    while True:
        
        if escolha.lower() == 'c':
            escolha_voltar = input(f'''
XXXXXXXX Cavaleiro XXXXXXXX

Vida:{usuario.vida}        Estamina:{usuario.estamina}
Força:{usuario.forca}        Defesa:{usuario.defesa}

XXXXXXXX           XXXXXXXX
Clique 'a' para voltar ''')
            if escolha_voltar == 'a':
               os.system('cls')
               print('voltando pro menu inical!')
               return
            else:
               print('opcão inválida!')
       
        elif escolha.lower() == 'm':
             escolha_voltar = input(f'''
XXXXXXXX Mago XXXXXXXX

Vida:{usuario.vida}        Mana:{usuario.mana}
Força:{usuario.forca}        Poder:{usuario.poder}

XXXXXXXX      XXXXXXXX
Clique 'a' para voltar ''')
             
             if escolha_voltar == 'a':
               os.system('cls')
               print('voltando pro menu inical!')
               return
             else:
               print('opcão inválida!')
            


    