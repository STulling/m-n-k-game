from game.cell import Cell
from game.position import Position

DEF_BOARD_SIZE = 10


class Board:
    """
    The playing field, on which the infinite game is played.

    Attributes:
        width       The width of the board.
        height      The height of the board.
        grid        The grid on which the game is played.
    """

    game = None
    width = None
    height = None
    grid = None

    def __init__(self, game=None, width=DEF_BOARD_SIZE, height=DEF_BOARD_SIZE):
        """
        Initialize the board with empty cells, based upon the specified size.

        :param width:   The width of the board.
        :param height:  The height of the board.
        """
        self.game = game
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y, self, self.game) for x in range(width)] for y in range(height)]

    def make_move(self, row, column, player):
        self.grid[column][row].activate(player)

    def get_cell(self, pos):
        return self.grid[pos.y][pos.x]

    def center(self):
        return Position(int(self.width/2), int(self.height/2))

    def __str__(self):
        string = ""
        for column in self.grid:
            string += str(column) + "\n"
        return string

    def __repr__(self):
        return str(self)
