from game.direction import Direction


class Position:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dir(self, direction):
        return {
            Direction.LEFT: Position(self.x-1, self.y),
            Direction.RIGHT: Position(self.x+1, self.y),
            Direction.UP: Position(self.x, self.y-1),
            Direction.DOWN: Position(self.x, self.y+1),
            Direction.UP_LEFT: Position(self.x-1, self.y-1),
            Direction.UP_RIGHT: Position(self.x+1, self.y-1),
            Direction.DOWN_LEFT: Position(self.x-1, self.y+1),
            Direction.DOWN_RIGHT: Position(self.x+1, self.y+1)
        }[direction]

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
