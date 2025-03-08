class mago():

    def __init__(self, vida, mana, forca, poder):
        self.vida = vida
        self.mana = mana
        self.forca = forca
        self.poder = poder
        
    def ataque_basico(self):
          ataque = self.forca
          print(f'Jogou uma bola de fogo {ataque}DM')
          return ataque

    def ataque_pesado(self):
        if self.mana > 0:
            ataque = self.poder*2
            self.mana -=1
            print(f'Jogou um meteoro {ataque}DM')
            return ataque
        else:
            print('O ataque falhou! não tem mana pra isso!')
    
    def habilidade (self):
        cura = self.poder - 5
        self.vida += cura
        print(f'Cura! {cura}DM')
    
    def ultimate(self):
        manaNecessaria = 5
        if self.mana > manaNecessaria:
            ataque = self.poder * 3
            self.mana -= manaNecessaria
            print(f'Chuva de meteoro! {ataque}DM')
            return ataque
        else:
            print('O ataque falhou! não tem mana pra isso!')
   
    def recebeu_dano(self, ataque):
        self.vida -= ataque
        
        
    