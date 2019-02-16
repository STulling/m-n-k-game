from game.occupation import Occupation
from game.direction import Direction
from game.position import Position


class Cell:
    """
    A cell on the board, on which the game is played.

    Attributes:
        occupied        The player who occupies the cell.
    """
    pos = None
    board = None
    game = None

    occupied = None
    player = None
    adjacency = None

    def __init__(self, x, y, board, game, occupied=Occupation.EMPTY):
        self.pos = Position(x, y)
        self.board = board
        self.game = game

        self.occupied = occupied
        self.adjacency = [{
            Direction.LEFT: 0,
            Direction.RIGHT: 0,
            Direction.UP: 0,
            Direction.DOWN: 0,
            Direction.UP_LEFT: 0,
            Direction.UP_RIGHT: 0,
            Direction.DOWN_LEFT: 0,
            Direction.DOWN_RIGHT: 0
        } for _ in range(2)]

    def activate(self, player):
        self.occupied = Occupation.FILLED
        self.player = player
        self.adjacency[self.game.current_player] = {
            Direction.LEFT: self.get_adjacent_value(Direction.LEFT),
            Direction.RIGHT: self.get_adjacent_value(Direction.RIGHT),
            Direction.UP: self.get_adjacent_value(Direction.UP),
            Direction.DOWN: self.get_adjacent_value(Direction.DOWN),
            Direction.UP_LEFT: self.get_adjacent_value(Direction.UP_LEFT),
            Direction.UP_RIGHT: self.get_adjacent_value(Direction.UP_RIGHT),
            Direction.DOWN_LEFT: self.get_adjacent_value(Direction.DOWN_LEFT),
            Direction.DOWN_RIGHT: self.get_adjacent_value(Direction.DOWN_RIGHT)
        }

    def get_adjacent_value(self, direction):
        res = self.board.get_cell(self.pos.to_dir(direction)).adjacency[self.game.current_player][direction] + 1
        if res >= self.game.win_length:
            self.game.win()
        return res

    def __str__(self):
        if self.player is None:
            return "0"
        return self.player.symbol

    def __repr__(self):
        return str(self)
