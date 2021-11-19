from game.actor import Actor
from game.point import Point
from game import constants


class Brick(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(constants.BRICK_HEIGHT)
        self.set_width(constants.BRICK_WIDTH)
        self.set_image(constants.IMAGE_BRICK_1)
        self._velocity = Point(2,0)

    def set_position(self, position):
        self._position = position
    def get_postiton(self):
        return self._position
    