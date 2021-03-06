import tkinter as tk
from functools import partial

from game.game import AdjGame
from game.player import Player, Computer


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
        self.title = tk.Label(self, text=self.game.players[self.game.current_player].name).grid(row=0)
        self.print = tk.Button(self, text="Debug", command=self.debug).grid(row=0, column=self.game.board.width - 1)
        self.create_grid()

    def create_grid(self):
        self.grid = [[tk.Button(self,
                                width=10,
                                height=5,
                                borderwidth=1,
                                command=partial(self.make_move, r, c)).grid(row=r + 1, column=c)
                      for r in range(self.game.board.height)]
                     for c in range(self.game.board.width)]
        if type(self.game) == AdjGame:
            c = self.game.board.center()
            self.grid[c.y][c.x] = tk.Button(self,
                                            width=10,
                                            height=5,
                                            text="X",
                                            borderwidth=1,
                                            bg=Application.get_color(self.game.current_player),
                                            command=partial(self.make_move, c.x, c.y)).grid(row=c.x + 1, column=c.y)

    def make_move(self, row, column):
        player = self.game.players[self.game.current_player]
        print(player)
        if type(player) == Player and player.make_move(row, column):
            self.grid[column][row] = tk.Button(self,
                                               width=10,
                                               height=5,
                                               text=player.symbol,
                                               borderwidth=1,
                                               bg=Application.get_color(self.game.current_player),
                                               command=lambda: self.make_move(row, column)).grid(row=row + 1,
                                                                                                 column=column)
            self.title = tk.Label(self, text=str(player)).grid(row=0)
        self.computer_move()

    def computer_move(self):
        player = self.game.players[self.game.current_player]
        if type(player) == Computer:
            pos = player.compute_move()
            self.grid[pos.y][pos.x] = tk.Button(self,
                                                width=10,
                                                height=5,
                                                text=player.symbol,
                                                borderwidth=1,
                                                command=lambda: self.make_move(pos.x, pos.y)).grid(row=pos.x + 1,
                                                                                                   column=pos.y)
            self.title = tk.Label(self, text=str(player)).grid(row=0)
            self.computer_move()

    @staticmethod
    def get_color(player):
        return {
            0: "red",
            1: "blue"
        }[player]

    def debug(self):
        print(self.game.board)
        for i in range(self.game.board.width):
            print(self.game.board.grid[0][i].adjacency)
