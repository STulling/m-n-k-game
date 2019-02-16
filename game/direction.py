from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

    @staticmethod
    def opp_dir(direction):
        return {
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.UP_LEFT: Direction.DOWN_RIGHT,
            Direction.UP_RIGHT: Direction.DOWN_LEFT,
            Direction.DOWN_LEFT: Direction.UP_RIGHT,
            Direction.DOWN_RIGHT: Direction.UP_LEFT
        }[direction]

    @staticmethod
    def main_dir(direction):
        return {
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.RIGHT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.DOWN,
            Direction.UP_LEFT: Direction.DOWN_RIGHT,
            Direction.UP_RIGHT: Direction.UP_RIGHT,
            Direction.DOWN_LEFT: Direction.UP_RIGHT,
            Direction.DOWN_RIGHT: Direction.DOWN_RIGHT
        }[direction]