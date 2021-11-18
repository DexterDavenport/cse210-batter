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
            velocity = Actor.get_velocity(ball)
            self._velocity = velocity * - 1
            audio_service.play_sound(constants.SOUND_BOUNCE)
            
            # print('this worked')
