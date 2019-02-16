

class Player:

    name = None
    symbol = None

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
