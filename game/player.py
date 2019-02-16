

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

    def __init__(self, name, symbol, game):
        super().__init__(name, symbol, game)
