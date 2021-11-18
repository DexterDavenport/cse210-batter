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
            x = -5
            y = -5
            ball.set_velocity(Point(x,y))
            audio_service.play_sound(constants.SOUND_BOUNCE)


        bricks = cast["bricks"]
        times_run = 0
        for brick in bricks:
            # print('it made it hear')
            if self._physics_service.is_collision(ball, brick):
                print('it made it hear')

                x = 5
                y = 5
                ball.set_velocity(Point(x,y))
                times_run += 1
                # print(times_run)
