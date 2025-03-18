import colorama
from colorama import Fore, Style
import os

colorama.init(autoreset=True)  # Inicializar colorama para Windows


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    limpiar_pantalla()
    print(Fore.CYAN + Style.BRIGHT + "🎮 MENÚ PRINCIPAL 🎮\n")
    print(Fore.YELLOW + "1️⃣  Jugar")
    print(Fore.GREEN + "2️⃣  Configuración")
    print(Fore.BLUE + "3️⃣  Acerca de")
    print(Fore.RED + "4️⃣  Salir\n")


def main():
    while True:
        mostrar_menu()
        opcion = input(Fore.MAGENTA + "👉 Selecciona una opción: ")

        if opcion == "1":
            print(Fore.YELLOW + "🎮 ¡Comenzando el juego!")
        elif opcion == "2":
            print(Fore.GREEN + "⚙️  Abriendo configuración...")
        elif opcion == "3":
            print(Fore.BLUE + "ℹ️  Este es un menú interactivo con Python y Colorama.")
        elif opcion == "4":
            print(Fore.RED + "👋 ¡Gracias por jugar! Hasta pronto.")
            break
        else:
            print(Fore.RED + "❌ Opción no válida, intenta de nuevo.")

        input(Fore.CYAN + "Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()
