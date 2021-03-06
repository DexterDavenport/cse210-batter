import os

os.environ['RAYLIB_BIN_PATH'] = '.'

from game import constants
from game.director import Director
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction 
from game.ball import Ball
from game.brick import Brick
from game.handle_off_screen_action import Handle_Off_Screen_Action
from game.paddle import Paddle
from game.handle_collisions_action import HandleCollisionsAction
from game.score import Score
from game.cloud import Cloud

def main():
    x = 1
    y = 20
    # create the cast {key: tag, value: list}
    cast = {}

    cast["score"] = []
    y1 = 470
    scores = []
    for brick in range(0, 3):
        y1 += 32

        score = Score()
        score.set_position(Point(10, y1))
        scores.append(score)
        cast["score"] = scores

    cast["cloud"] = []
    clouds = []

    cloud = Cloud()
    cloud.set_position(Point(400, 150))
    clouds.append(cloud)
    cast["cloud"] = clouds



    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    bricks = []
    
    num = 0

    for brick in range(0, 112):
        brick = Brick()
        # brick.set_image(constants.IMAGE_BRICK_2)
        num += 1

        if x > 800:
            x = 1
            y += 40
        # This is what makes the American Flag theme
        if x < 200 and (y == 20 or 60 or 100 or 140):
            brick.set_image(constants.IMAGE_BRICK_2)
        if x > 200 or y ==180:
            brick.set_image(constants.IMAGE_BRICK_1)
        if y ==60 and x > 200:
            brick.set_image(constants.IMAGE_BRICK_3)
        if y ==140:
            brick.set_image(constants.IMAGE_BRICK_3)
        if y ==220:
            brick.set_image(constants.IMAGE_BRICK_3)
        if y ==260:
            brick.set_image(constants.IMAGE_BRICK_1)

        brick.set_position(Point(x, y))
        
        x += 50

        bricks.append(brick)
    cast["bricks"] = bricks

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    balls = []
    ball = Ball()
    ball.set_position(Point(380, 500))
    balls.append(ball)
    cast["balls"] = balls

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list
    paddles = []
    paddle = Paddle()
    paddle.set_position(Point(345, 530))
    paddles.append(paddle)
    cast["paddle"] = paddles

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)
    handle_off_screen_action = Handle_Off_Screen_Action(physics_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,handle_collisions_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()