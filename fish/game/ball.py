from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(0)
        self.set_width(0)
        # self.set_image(constants.IMAGE_BALL)
        self._velocity = Point(0,0)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position
