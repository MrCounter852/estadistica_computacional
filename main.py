from movimiento_aleatorio import Camino_tradicional
from Campo import campo
from Coordenada import coordenada


def simular_caminata(pasos, numero_tries, tipo_aleatorio):
    aleat = tipo_aleatorio(nombre = "camino_1")
    origen = coordenada(0, 0)
    distancias = []

    for i in range(numero_tries):
        Campo = campo()
        campo.anadir_aleatorio(aleat, origen)
    

def main(distancias_c, numero_tries, tipo_aleatorio):
    for pasos in distancias_c:
        distancias = simular_caminata(pasos, numero_tries, tipo_aleatorio)


if __name__ == "__main__":
    distancias_c = [10, 100, 1000, 10000]
    numero_tries = 100
    main(distancias_c, numero_tries, Camino_tradicional)