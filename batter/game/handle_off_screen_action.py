# from game.constants import MAX_X
from game.action import Action
from game import constants
from game.point import Point


class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        # if self._physics_service.is_collision(ball, paddle):
        #     self._velocity = Point(-5,-5)
        #     print('wrong thing')


    