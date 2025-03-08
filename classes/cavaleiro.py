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
        return ataque

    def ataque_pesado(self):
        if self.estamina > 0:
            ataque = self.forca*2
            self.estamina -=1
            print(f'Ataque pesado! {ataque} DM')
            return ataque
        else:
            print('Não tem estamina pra isso!')

    def  habilidade(self):
        if self.status_defesa == True:
            print('O escudo ainda esta ativo !')
        else:
            self.status_defesa = True
            print('Levantou o escudo!')
      
    def ultimate(self):
        estamina_necessaria = 5
        if self.estamina > estamina_necessaria:
            ataque = self.forca * 3
            self.estamina -= estamina_necessaria
            print(f'ataque pesado realizado{ataque}')
            return ataque
        else:
            print('O ataque falhou! não tem estamina pra isso!')
            return 0
   
    def recebeu_dano(self, dano):
        if self.status_defesa == True and self.defesa >= dano:
            print('O escudo defendeu o ataque! ')
        elif self.status_defesa == True and self.defesa < dano:
            ataque = dano - self.defesa
            self.vida -= ataque
        else:
            self.vida -= dano
            

        
