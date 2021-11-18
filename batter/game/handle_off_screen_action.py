# from game.constants import MAX_X
from game.action import Action
from game import constants
from game.point import Point


class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        ball = cast["balls"][0]
        bricks = cast["bricks"]
        times_run = 0
        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                x = 5
                y = 5
                ball.set_velocity(Point(x,y))
                times_run += 1
                print(times_run)


    