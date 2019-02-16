from game.occupation import Occupation
from game.player import Player
from game.board import Board


class Game:
    players = None
    board = None

    current_player = None
    win_length = 3

    def __init__(self):
        self.players = [Player("Player 1", "X"), Player("Player 2", "T")]
        self.board = Board(game=self)
        self.current_player = 0

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
