class Adivinanza:

    def __init__(self, palabra: str):
        self.__ltr: list[str] = list(palabra)
        self.__pos: list[bool] = [False] * len(self.__ltr)

    def adivinar(self, l: str) -> [int]:

        if l not in self.__ltr:
            return []

        p_l = []
        for i in range(len(self.__ltr)):
            if self.__ltr[i] == l:
                p_l.append(i)
                self.__pos[i] = True
        return p_l

    def obtener_letras(self) -> [str]:

        return self.__ltr

    def obtener_posiciones(self) -> [bool]:

        return self.__pos

    def obtener_cantidad_posiciones(self) -> int:

        return len(self.__ltr)

    def verificar_si_hay_triunfo(self) -> bool:

        return all(self.__pos)
