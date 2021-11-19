from game.action import Action
from game import constants
from game.point import Point
from game.audio_service import AudioService
from game.actor import Actor

audio_service = AudioService()

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]

        if self._physics_service.is_collision(ball, paddle):
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))



        bricks = cast["bricks"]
        # times_run = 0
        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))

                # ball.set_velocity(Point(x,y))
                bricks.remove(brick)
                # times_run += 1
                # print(times_run)


