import random
from classes.mago import mago
from classes.cavaleiro import cavaleiro

def bot_classe():
    bot_classe = random.randint(1,2)
    
    if bot_classe == 1:
        bot = mago(vida=100 , mana=50, forca=40, poder=10)
        print('Seu inimigo é um mago!')
        return bot
    elif bot_classe == 2:
        bot = cavaleiro(vida=150, forca=15, estamina=4, defesa=10, status_defesa=False)
        print('Seu inimigo é um cavaleiro!')
        return bot