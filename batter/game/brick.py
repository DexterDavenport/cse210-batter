from actor import Actor
from game.point import Point

class Brick(Actor):
    def _init__(self):
        super().__init__()

    def set_position(self, position):
        self._position = position
    