from game.direction import Direction
from game.occupation import Occupation
from game.player import *
from game.board import Board
from game.position import Position


DEF_BOARD_SIZE = 10
DEF_WIN_LENGTH = 3


class Game:
    players = None
    board = None

    current_player = None
    win_length = None

    def __init__(self, m=DEF_BOARD_SIZE, n=DEF_BOARD_SIZE, k=DEF_WIN_LENGTH):
        self.players = [Player("Player 1", "X", self), Player("Player 2", "T", self)]
        self.current_player = 0

        self.board = Board(m, n, game=self)
        self.win_length = k

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def make_move(self, row, column):
        if self.valid_move(row, column):
            self.board.make_move(row, column, self.players[self.current_player])
            self.next_player()
            return True
        return False

    def valid_move(self, row, column):
        return self.board.grid[column][row].occupied != Occupation.FILLED

    def win(self):
        print("WIN")


class AdjGame(Game):

    def __init__(self, m=DEF_BOARD_SIZE, n=DEF_BOARD_SIZE, k=DEF_WIN_LENGTH):
        super().__init__(n, m, k)
        pos = self.board.center()
        self.board.make_move(pos.x, pos.y, self.players[self.current_player])
        self.next_player()

    def valid_move(self, row, column):
        for direction in Direction.dir_list():
            if self.board.get_cell(Position(row, column).to_dir(direction)).occupied == Occupation.FILLED:
                return True
        return False


class AIGame(Game):

    game = None

    def __init__(self, game):
        super().__init__(m=game.board.width, n=game.board.height, k=game.win_length)
        self.game = game
        self.players = [Player("Player 1", "X", self), Computer("Computer 2", "T", self)]

    def make_move(self, row, column):
        if self.game.make_move(row, column):
            self.next_player()
            return True
        return False

    def __str__(self):
        return str(self.game)

    def __repr__(self):
        return str(self.game)

    def valid_move(self, row, column):
        return self.game.valid_move(row, column)
