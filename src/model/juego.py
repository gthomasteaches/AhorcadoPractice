from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self, dificultad: str):
        self.dificultad = dificultad
        self.intentos_permitidos: int = 0
        self.diccionario = Diccionario()
        self.adivinanza: Adivinanza = None

    def __generar_palabra(self) -> str:
        return self.diccionario.obtener_palabra()

    def __calcular_intentos_permitidos(self, dificultad: str) -> int:
        if dificultad == self.DIFICULTAD_BAJA:
            return 20
        if dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def iniciar_partida(self) -> int:
        palabra = self.__generar_palabra()
        self.adivinanza: Adivinanza = Adivinanza(palabra)
        self.intentos_permitidos = self.__calcular_intentos_permitidos(self.dificultad)
        return self.adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        if self.intentos_permitidos < 0:
            raise ErrorIntentosInsuficientes()
        self.intentos_permitidos -= 1
        return self.adivinanza.adivinar(letra)

    def verificar_si_juego_continua(self) -> bool:
        return self.intentos_permitidos >= 0 and self.adivinanza.verificar_si_hay_triunfo()

    def verificar_triunfo(self) -> bool:
        return self.adivinanza.verificar_si_hay_triunfo()
