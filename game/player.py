from game.position import Position
from solver.minimax import Minimax


class Player:

    name = None
    symbol = None
    game = None

    def __init__(self, name, symbol, game):
        self.name = name
        self.symbol = symbol
        self.game = game

    def make_move(self, row, col):
        return self.game.make_move(row, col)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Computer(Player):

    algorithm = None

    def __init__(self, name, symbol, game, algorithm=Minimax()):
        super().__init__(name, symbol, game)
        self.algorithm = algorithm

    def compute_move(self):
        pos = self.algorithm.exec(self.game.board)
        if self.game.make_move(pos.x, pos.y):
            return pos
        return Position(-1,-1)

