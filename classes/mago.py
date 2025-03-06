class mago():

    def __init__(self, vida, mana, forca, poder):
        self.vida = vida
        self.mana = mana
        self.forca = forca
        self.poder = poder
        
    def ataque_basico(self):
          ataque = self.poder
          print(f'Jogou uma bola de fogo {ataque}DM')

    def ataque_pesado(self):
        if self.mana > 0:
            ataque = self.poder*2
            self.mana -=1
            print(f'Jogou um meteoro {ataque}DM')
        else:
            print('O ataque falhou! não tem mana pra isso!')
    
    def ultimate(self):
        manaNecessaria = 5
        if self.mana > manaNecessaria:
            ataque = self.poder * 3
            self.mana -= manaNecessaria
        else:
            print('O ataque falhou! não tem mana pra isso!')
   
    def recebendo_dano(self, dano):
        self.vida -= dano
        print('apanhou')
    