import tkinter as tk
from functools import partial


class Application(tk.Frame):

    game = None
    grid = None
    title = None

    def __init__(self, master=None, game=None):
        super().__init__(master)
        self.master = master
        self.game = game
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Player 1").grid(row=0)
        self.print = tk.Button(self, text="Debug", command=self.debug).grid(row=0, column=9)
        self.create_grid()

    def create_grid(self):
        self.grid = [[tk.Button(self,
                               width=10,
                               height=5,
                               text="0",
                               borderwidth=1,
                               command=partial(self.make_move, r, c)).grid(row=r+1, column=c)
                     for r in range(10)]
                     for c in range(10)]

    def make_move(self, row, column):
        player = self.game.players[self.game.current_player]
        if self.game.make_move(row, column):
            self.grid[column][row] = tk.Button(self,
                                   width=10,
                                   height=5,
                                   text=player.symbol,
                                   borderwidth=1,
                                   command=lambda: self.make_move(row, column)).grid(row=row+1, column=column)
            self.title = tk.Label(self, text=str(player)).grid(row=0)

    def debug(self):
        print(self.game.board)
        for i in range(10):
            print(self.game.board.grid[0][i].adjacency)
