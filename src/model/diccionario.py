import random


class Diccionario:
    def __init__(self):
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        palabras = []
        with open("assets/palabras.txt", "r") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self) -> str:
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
