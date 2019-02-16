from game.occupation import Occupation


class Cell:
    """
    A cell on the board, on which the game is played.

    Attributes:
        occupied        The player who occupies the cell.
    """
    occupied = None

    def __init__(self, occupied=Occupation.EMPTY):
        self.occupied = occupied

    def __str__(self):
        return str(self.occupied.value)

    def __repr__(self):
        return  str(self)