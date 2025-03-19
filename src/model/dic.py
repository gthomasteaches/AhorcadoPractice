import random


class Dic:

    def __init__(self):
        self.plbs: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        plbs = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                plbs.append(line.strip())

        return plbs

    def obtener_palabra(self) -> str:
        i_a = random.randint(0, len(self.plbs) - 1)
        return self.plbs[i_a]
