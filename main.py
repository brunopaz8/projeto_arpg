from classes.bot import bot_classe
from menu.menu_inicial.menu_classe import escolha_classe
from menu.menu_inicial.criando_personagem import criando_personagem
from menu.menu_principal import menu_principal
from menu.menu_batalha.cavaleiro_batalha import batalha_cavaleiro
from menu.menu_batalha.mago_batalha import batalha_mago


escolha = escolha_classe()
usuario = criando_personagem(escolha= escolha)

if escolha.lower() == 'c':
    menu_principal(usuario= usuario, escolha= escolha)
    bot = bot_classe()
    batalha_cavaleiro(usuario= usuario, bot= bot)
    menu_principal(usuario= usuario, escolha= escolha)

elif escolha.lower() == 'm':
    menu_principal(usuario= usuario, escolha= escolha)
    bot = bot_classe()
    batalha_mago(usuario= usuario, bot= bot)
    menu_principal(usuario= usuario, escolha= escolha)
    
    








    
    
    