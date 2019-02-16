from game.game import Game
from gui.gui import Application
import tkinter as tk

def main():
    root = tk.Tk()
    app = Application(master=root, game=Game())
    app.mainloop()


if __name__ == "__main__":
    main()