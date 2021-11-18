from game.actor import Actor
from game.point import Point
from game import constants


class Paddle(Actor):
    def __init__(self):
        super().__init__()
        # self.set_position(Point(345, 530))
        self.set_image(constants.IMAGE_PADDLE)
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)