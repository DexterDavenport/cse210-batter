from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService
import random


audio_service = AudioService()


class Handle_Off_Screen_Action(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service


    def execute(self, cast):
        
        ball = cast["balls"][0]
        fish = cast["fish"][0]
        scores = cast["score"]
        shark = cast["shark"][0]
        shark1 = cast["shark"][1]
        shark2 = cast["shark"][2]


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
            fish.set_position(Point(345, 530))
            ball.set_position(Point(380, 500))

        if shark.get_position().get_x() <= 50:
            y = random.randint(0,550)
            shark.set_position(Point(776, y))
        if shark1.get_position().get_x() <= 50:
            y = random.randint(0,550)
            shark1.set_position(Point(776, y))
        if shark2.get_position().get_x() <= 50:
            y = random.randint(0,550)
            shark2.set_position(Point(776, y))
            
            
            # for score in scores:
            scores.pop(0)
