class cavaleiro:
    def __init__(self, vida, forca,estamina, defesa, status_defesa):
        self.vida = vida
        self.forca = forca
        self.estamina = estamina
        self.defesa = defesa
        self.status_defesa = status_defesa
    
    def ataque_basico(self):
        ataque = self.forca
        print(f'Você atacou com a espada causando {ataque} DM')

    def ataque_pesado(self):
        if self.estamina > 0:
            ataque = self.forca*2
            self.estamina -=1
            print(f'você jogou um meteoro {ataque} DM')
        else:
            print('você não tem mana pra isso')

    def  escudo(self):
        if self.status_defesa == True:
            print('O escudo ainda esta ativo !')
        else:
            self.status_defesa = True
            print('Voce preparou o escudo!')
      
    def ultimate(self):
        estamina_necessaria = 5
        if self.estamina > estamina_necessaria:
            ataque = self.poder * 3
            self.estamina -= estamina_necessaria
            print(f'ataque pesado realizado')
        else:
            print('O ataque falhou! Você não tem mana pra isso!')
   
    def recebendo_dano(self, dano):
        if self.status_defesa == True and self.defesa >= dano:
            print('Voce defendeu o ataque')
        elif self.status_defesa == True and self.defesa < dano:
            ataque = dano - self.defesa
            self.vida -= ataque
            print(f'Voce tomou {ataque} de dano')
        else:
            self.vida -= dano
            print(f'Voce tomou: {dano}DM')

        
