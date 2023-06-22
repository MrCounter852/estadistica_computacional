
import random 
class aleatorio:
    def __init__(self, nombre):
        self.nombre = nombre



class Camino_tradicional(aleatorio):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina():
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])