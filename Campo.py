class campo:
    def __init__(self):
        self.coordenadas_aleatorias = {}

    def anadir_aleatorio(self, aleatorio, coordenada):
        self.coordenadas_aleatorias[aleatorio] = coordenada

    def mover_aleatorio(self, aleatorio):
        deltax, deltay = aleatorio.camina()
        coordenada_actual = self.coordenadas_aleatorias[aleatorio]
        nueva_coordenada = coordenada_actual.mover(deltax, deltay)

    def obtener_coordenada(self, aleatorio):
        return self.coordenadas_aleatorias[aleatorio]