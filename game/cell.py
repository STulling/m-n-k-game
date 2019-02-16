from game.occupation import Occupation
from game.direction import Direction
from game.position import Position
from game.union_find import UnionFind


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
            Direction.RIGHT: UnionFind(None, 0),
            Direction.DOWN: UnionFind(None, 0),
            Direction.UP_RIGHT: UnionFind(None, 0),
            Direction.DOWN_RIGHT: UnionFind(None, 0)
        } for _ in range(2)]

    def activate(self, player):
        self.occupied = Occupation.FILLED
        self.player = player
        self.mnk_update()

    def mnk_update(self):
        self.adjacency[self.game.current_player] = {
            Direction.RIGHT: self.get_adjacent_value(Direction.RIGHT),
            Direction.DOWN: self.get_adjacent_value(Direction.DOWN),
            Direction.UP_RIGHT: self.get_adjacent_value(Direction.UP_RIGHT),
            Direction.DOWN_RIGHT: self.get_adjacent_value(Direction.DOWN_RIGHT)
        }

    def mnk_get_value(self, direction):
        return self.board.get_cell(self.pos.to_dir(direction)).adjacency[self.game.current_player][Direction.main_dir(direction)]

    def get_adjacent_value(self, direction):
        s_res = self.mnk_get_value(direction)
        o_res = self.mnk_get_value(Direction.opp_dir(direction))

        if s_res.rank > 0:
            self.adjacency[self.game.current_player][Direction.main_dir(direction)].union(s_res)
        if o_res.rank > 0:
            self.adjacency[self.game.current_player][Direction.main_dir(direction)].union(o_res)

        self.adjacency[self.game.current_player][Direction.main_dir(direction)].rank += 1

        if self.adjacency[self.game.current_player][Direction.main_dir(direction)].rank >= self.game.win_length:
            self.game.win()
        return self.adjacency[self.game.current_player][Direction.main_dir(direction)]

    def __str__(self):
        if self.player is None:
            return "0"
        return self.player.symbol

    def __repr__(self):
        return str(self)
