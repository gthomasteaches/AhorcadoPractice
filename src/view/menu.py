import colorama
from colorama import Fore, Style
from src.model.juego import Juego


class Menu:

    def __init__(self, juego: Juego):
        colorama.init(autoreset=True)  # Inicializar colorama para Windows
        self.juego: Juego = juego

    def __opciones(self):
        print(Fore.CYAN + Style.BRIGHT + "🎮 MENÚ PRINCIPAL 🎮\n")
        print(Fore.YELLOW + "1️⃣  Jugar")
        print(Fore.GREEN + "2️⃣  Configuración")
        print(Fore.BLUE + "3️⃣  Salir\n")

    def __letra(self) -> list[int]:
        letra = input(Fore.YELLOW + "🎮 ¡Ingresa una letra!: ")
        return self.juego.adivinar(letra)

    def __configuracion(self):
        print(Fore.GREEN + "1️⃣  Dificultad Baja")
        print(Fore.GREEN + "2️⃣  Dificultad Media")
        print(Fore.GREEN + "3️⃣  Dificultad Alta")
        opcion = input(Fore.YELLOW + "🎮 ¡Selecciona la dificultad con la que deseas jugar!: ")

        if opcion == "1":
            self.juego.modificar_dificultad(Juego.D_B)
        elif opcion == "2":
            self.juego.modificar_dificultad(Juego.D_M)
        elif opcion == "3":
            self.juego.modificar_dificultad(Juego.D_A)

    def __menu_1(self):
        cantidad_posiciones = self.juego.iniciar_partida()
        display = Fore.RED + " _ " * cantidad_posiciones
        print(display)

        while True:
            if self.juego.verificar_triunfo():
                print(Fore.GREEN + "🎮 ¡Felicitaciones! ¡Has ganado!")
                break
            if not self.juego.verificar_si_hay_intentos():
                print(Fore.RED + "🎮 ¡Lo siento! ¡Has superado el máximo de intentos!")
                break

            intentos_permitidos = self.juego.calcular_intentos_permitidos()
            intentos_realizados = intentos_permitidos - self.juego.obtener_intentos_realizados()
            letra = input(Fore.YELLOW + f"🎮 ¡Ingresa una letra! ({intentos_realizados}/{intentos_permitidos}) ").upper()
            resultado_adivinanza = self.juego.adivinar(letra)
            self.__resultado_jugada(resultado_adivinanza)

    def __adivinanza(self):
        letras = self.juego.obtener_adivinanza().obtener_letras()
        posiciones = self.juego.obtener_adivinanza().obtener_posiciones()
        display = ""
        for i in range(len(letras)):
            if posiciones[i]:
                display += Fore.GREEN + " " + letras[i] + " "
            else:
                display += Fore.RED + " _ "

        print(display)

    def __resultado_jugada(self, resultado_adivinanza: list[int]):
        if len(resultado_adivinanza) == 0:
            print(Fore.YELLOW + "¡Lo siento, no has acertado! ¡Sigue intentando!")
        else:
            print(Fore.YELLOW + "¡Muy bien, has acertado! ¡Sigue así!")
        self.__adivinanza()

    def inicio(self):
        while True:
            self.__opciones()
            opcion = input(Fore.MAGENTA + "👉 Selecciona una opción: ")

            if opcion == "1":
                print(Fore.YELLOW + "🎮 ¡Comenzando el juego!")
                self.__menu_1()
            elif opcion == "2":
                print(Fore.GREEN + "⚙️  Abriendo configuración...")
                self.__configuracion()
            elif opcion == "3":
                exit()
            else:
                print(Fore.RED + "❌ Opción no válida, intenta de nuevo.")
