from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService


audio_service = AudioService()


class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service


    def execute(self, cast):
        
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        scores = cast["score"]


        if ball.get_position().get_x() <= 1:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        if ball.get_position().get_x() >= 776:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        if ball.get_position().get_y() <= 0:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        if ball.get_position().get_y() >= 576:
            audio_service.play_sound(constants.SOUND_BOUNCE)
            paddle.set_position(Point(345, 530))
            ball.set_position(Point(380, 500))
            
            # for score in scores:
            scores.pop(0)
