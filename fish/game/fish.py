from game.actor import Actor
from game.point import Point
from game import constants


class Fish(Actor):
    def __init__(self):
        super().__init__()
        # self.set_position(Point(345, 530))
        self.set_image(constants.IMAGE_FISH)
        self.set_width(constants.FISH_WIDTH)
        self.set_height(constants.FISH_HEIGHT)