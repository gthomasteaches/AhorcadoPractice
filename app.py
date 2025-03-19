from src.model.juego import Juego

from src.view.menu import Menu

if __name__ == "__main__":
    juego: Juego = Juego()
    menu: Menu = Menu(juego)
    menu.iniciar()
