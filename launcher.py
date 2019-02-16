from game.game import *
from gui.gui import Application
import tkinter as tk

BOARD_SIZE = 5
WIN_LENGTH = 3


def main():
    root = tk.Tk()
    app = Application(master=root, game=AIGame(Game(m=BOARD_SIZE, n=BOARD_SIZE, k=3)))
    app.mainloop()


if __name__ == "__main__":
    main()