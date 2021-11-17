from game.actor import Actor
from game.point import Point

class Ball(Actor):
    def _init__(self):
        super().__init__()
        self._velocity = (5,5)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position