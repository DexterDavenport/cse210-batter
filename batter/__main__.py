import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.control_actors_action import ControlActorsAction
# from game.move_actor_action import MoveActorsAction 

# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction

def main():
    x = 1
    y = 20

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    bricks = []
    balls = []
    
    for brick in range(0, 112):
        brick = Actor()
        brick.set_image(constants.IMAGE_BRICK_2)

        if x > 751:
            x = 1
            y += 40
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
        # brick.set_image(constants.IMAGE_BRICK)
        brick.set_width(constants.BRICK_WIDTH)
        brick.set_height(constants.BRICK_HEIGHT)
        bricks.append(brick)
    cast["bricks"] = bricks

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    ball = Actor()
    ball.set_position(Point(380, 500))
    ball.set_image(constants.IMAGE_BALL)
    ball.set_width(constants.BALL_WIDTH)
    ball.set_height(constants.BALL_HEIGHT)
    ball.get_position()
    # MoveActorsAction._move_actor(ball)

    balls.append(ball)
    cast["balls"] = balls

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list
    paddles = []
    paddle = Actor()
    paddle.set_position(Point(345, 530))
    paddle.set_image(constants.IMAGE_PADDLE)
    paddle.set_width(constants.PADDLE_WIDTH)
    paddle.set_height(constants.PADDLE_HEIGHT)
    paddles.append(paddle)
    cast["paddle"] = paddles

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = []
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
