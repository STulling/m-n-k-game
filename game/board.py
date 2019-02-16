from game.cell import Cell
from game.direction import Direction
from game.position import Position


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

    def __init__(self, width, height, game=None):
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
        try:
            return self.grid[pos.y][pos.x]
        except IndexError:
            return Cell(-1, -1, self, self.game)

    def center(self):
        return Position(int(self.width/2), int(self.height/2))

    def expand(self, dir):
        if dir is Direction.LEFT:
            for row in self.grid:
                for cell in row:
                    cell.move_cell(self.width, 0)
            self.grid = [[Cell(x, y, self, self.game) for x in range(self.width)] for y in
                                     range(self.height)] + self.grid
            return
        if dir is Direction.RIGHT:
            self.grid = self.grid + [[Cell(x, self.height + y, self, self.game) for x in range(self.width)] for y in range(self.height)]
            return
        if dir is Direction.UP:
            for row in self.grid:
                for cell in row:
                    cell.move_cell(0, self.height)
            for y in range(self.height):
                self.grid[y] = [Cell(x, y, self, self.game) for x in range(self.width)] + self.grid[y]
            return
        if dir is Direction.DOWN:
            for y in range(self.height):
                self.grid[y] = self.grid[y] + [Cell(self.width + x, y, self, self.game) for x in range(self.width)]
            return

    def __str__(self):
        string = ""
        for column in self.grid:
            string += str(column) + "\n"
        return string

    def __repr__(self):
        return str(self)
