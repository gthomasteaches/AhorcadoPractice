from src.model.dic import Dic
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:
    D_B = "DIFICULTAD_BAJA"
    D_M = "DIFICULTAD_MEDIA"
    D_A = "DIFICULTAD_ALTA"

    def __init__(self):
        self.__dif = Juego.D_B
        self.__intentos: int = 0
        self.__dic = Dic()
        self.__adiv: Adivinanza = None

    def obtener_intentos_realizados(self):
        return self.__intentos

    def obtener_adivinanza(self) -> Adivinanza:

        return self.__adiv

    def __generar_palabra(self) -> str:
        return self.__dic.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        if self.__dif == self.D_B:
            return 20
        if self.__dif == self.D_M:
            return 10
        if self.__dif == self.D_A:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        self.__dif = dificultad

    def iniciar_partida(self) -> int:
        palabra = self.__generar_palabra()
        self.__adiv: Adivinanza = Adivinanza(palabra)
        self.__intentos = self.calcular_intentos_permitidos()
        return self.__adiv.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        if self.__intentos < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos -= 1
        return self.__adiv.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        return self.__intentos >= 0

    def verificar_triunfo(self) -> bool:
        return self.__adiv.verificar_si_hay_triunfo()
