from classes.mago import mago
from classes.cavaleiro import cavaleiro


usuario = cavaleiro(vida=150, forca=15,estamina=4, defesa=10, status_defesa=False)

usuario.ataque_pesado()
usuario.escudo()
usuario.recebendo_dano(8)
usuario.recebendo_dano(12)