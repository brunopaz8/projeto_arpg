import os

def cavaleiro_batalha(usuario, bot):
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