from game.cell import Cell

DEF_BOARD_SIZE = 20


class Board:
    """
    The playing field, on which the infinite game is played.

    Attributes:
        width       The width of the board.
        height      The height of the board.
        grid        The grid on which the game is played.
    """
    width = None
    height = None
    grid = None

    def __init__(self, width=DEF_BOARD_SIZE, height=DEF_BOARD_SIZE):
        """
        Initialize the board with empty cells, based upon the specified size.

        :param width:   The width of the board.
        :param height:  The height of the board.
        """
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

    def __str__(self):
        string = ""
        for column in self.grid:
            string += str(column) + "\n"
        return string

    def __repr__(self):
        return str(self)
