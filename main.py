from classes.bot import bot_classe
from menu.menu_inicial.menu_classe import escolha_classe
from menu.menu_inicial.menu_principal import menu_principal
from menu.menu_batalha.cavaleiro_batalha import batalha_cavaleiro

import os
import random


usuario = escolha_classe()

menu_principal()

bot = bot_classe()

batalha_cavaleiro(usuario= usuario, bot= bot)


    
    
    