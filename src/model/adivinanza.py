class Adivinanza:
    def __init__(self, palabra: str):
        self.palabra: list[str] = palabra.split("")
        self.posiciones: list[bool] = [False] * len(self.palabra)

    def adivinar(self, letra: str) -> [int]:
        if letra not in self.palabra:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.palabra)):
            if self.palabra[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_cantidad_posiciones(self) -> int:
        return len(self.palabra)

    def verificar_si_hay_triunfo(self) -> bool:
        return all(self.posiciones)
