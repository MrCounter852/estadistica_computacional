class coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, deltax, deltay):
        return coordenada(self.x + deltax, self.y + deltay)
    
    def distancia(self, otra_coordenada):
        deltax = self.x - otra_coordenada.x
        deltay = self.y - otra_coordenada.y
        return (deltax**2 + deltay**2)**0.5
    