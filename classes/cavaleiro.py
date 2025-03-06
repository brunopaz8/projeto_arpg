class cavaleiro:
    def __init__(self, vida, forca,estamina, defesa, status_defesa):
        self.vida = vida
        self.forca = forca
        self.estamina = estamina
        self.defesa = defesa
        self.status_defesa = status_defesa
    
    def ataque_basico(self):
        ataque = self.forca
        print(f'Atacou com a espada! causando {ataque} DM')

    def ataque_pesado(self):
        if self.estamina > 0:
            ataque = self.forca*2
            self.estamina -=1
            print(f'Usou o ataque pesado! {ataque} DM')
        else:
            print('Não tem estamina pra isso!')

    def  escudo(self):
        if self.status_defesa == True:
            print('O escudo ainda esta ativo !')
        else:
            self.status_defesa = True
            print('Levantou o escudo!')
      
    def ultimate(self):
        estamina_necessaria = 5
        if self.estamina > estamina_necessaria:
            ataque = self.poder * 3
            self.estamina -= estamina_necessaria
            print(f'ataque pesado realizado{ataque}')
        else:
            print('O ataque falhou! não tem estamina pra isso!')
   
    def recebendo_dano(self, dano):
        if self.status_defesa == True and self.defesa >= dano:
            print('Defendeu o ataque')
        elif self.status_defesa == True and self.defesa < dano:
            ataque = dano - self.defesa
            self.vida -= ataque
            print(f'Tomou {ataque} de dano')
        else:
            self.vida -= dano
            print(f'Tomou: {dano}DM')

        
