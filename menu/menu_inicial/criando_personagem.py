from classes.cavaleiro import cavaleiro
from classes.mago import mago
import os


def criando_personagem(escolha):
    vida_cavaleiro = 120
    forca_cavaleiro = 13
    estamina = 15
    defesa = 5
    vida_mago = 100
    forca_mago = 10
    mana = 20
    poder = 15
    pontos = 4
    
    while True:
        if escolha.lower() == 'c':
            
            escolha_status = input(f'''
XXXXXXXX Cavaleiro XXXXXXXX

Você tem: {pontos} pontos restantes

[a]Vida:{vida_cavaleiro}+        [d]Estamina:{estamina}+
[s]Força:{forca_cavaleiro}+        [f]Defesa:{defesa}+

Para confirmar as mudanças selecione 'q'!

XXXXXXXX           XXXXXXXX
Sua escolha: ''')
            if escolha_status.lower() == 'a' and pontos > 0:
               os.system('cls')
               print('vida aumentada!')
               vida_cavaleiro += 5
               pontos -= 1
           
            elif escolha_status.lower() == 's' and pontos > 0:
                os.system('cls')
                print('Força aumentada!')
                forca_cavaleiro += 5
                pontos -= 1
            
            elif escolha_status.lower() == 'd' and pontos > 0:
                os.system('cls')
                print('Estamina aumentada!')
                estamina += 5
                pontos -= 1
            
            elif escolha_status.lower() == 'f' and pontos > 0:
                os.system('cls')
                print('Defesa aumentada!')
                defesa += 5
                pontos -= 1
           
            elif escolha_status.lower() == 'q' and pontos == 0:
                os.system('cls')
                print('Cavaleiro criado!')
                usuario = cavaleiro(vida= vida_cavaleiro, forca= forca_cavaleiro, estamina= estamina, defesa= defesa, status_defesa= False)
                return usuario
            
            elif escolha_status.lower() == 'q' and pontos >0:
                os.system('cls')
                print('você ainda tem pontos para gastar!')

            elif escolha_status.lower() == ['a','s','d','f'] and pontos == 0:
                os.system('cls')
                print('você não tem pontos o suficiente!')
    
            else:
               os.system('cls')
               print('opcão inválida!')
        
        elif escolha.lower() == 'm':
             escolha_status = input(f'''
XXXXXXXX Mago XXXXXXXX

Você tem: {pontos} pontos restantes

[a]Vida:{vida_mago}+        [d]Mana:{mana}+
[s]Força:{forca_mago}+        [f]Poder:{poder}+

Para confirmar as mudanças selecione 'q'!

XXXXXXXX      XXXXXXXX
Sua escolha: ''')
             
             
             if escolha_status.lower() == 'a' and pontos > 0:
                os.system('cls')
                print('vida aumentada!')
                vida_mago += 5
                pontos -= 1
           
             elif escolha_status.lower() == 's' and pontos > 0:
                os.system('cls')
                print('Força aumentada!')
                forca_mago += 5
                pontos -= 1
            
             elif escolha_status.lower() == 'd' and pontos > 0:
                os.system('cls')
                print('Mana aumentada!')
                mana += 5
                pontos -= 1
            
             elif escolha_status.lower() == 'f' and pontos > 0:
                os.system('cls')
                print('Poder aumentado!')
                poder += 5
                pontos -= 1
           
             elif escolha_status.lower() == 'q' and pontos == 0:
                os.system('cls')
                print('Mago criado!')
                usuario = mago(vida= vida_mago, mana= mana, forca= forca_mago, poder= poder)
                return usuario
            
             elif escolha_status.lower() == 'q' and pontos > 0:
                os.system('cls')
                print('você ainda tem pontos para gastar!')

             elif escolha_status.lower() == ['a','s','d','f'] and pontos == 0:
                os.system('cls')
                print('você não tem pontos o suficiente!')
    
             else:
                os.system('cls')
                print('opcão inválida!')