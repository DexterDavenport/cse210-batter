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

# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    # TODO: Create bricks here and add them to the list
    bricks = []
    

    brick1 = Actor()
    brick1.set_position(Point(10, 10))
    brick1.set_image(constants.IMAGE_BRICK)
    brick1.set_width(constants.BRICK_WIDTH)
    brick1.set_height(constants.BRICK_HEIGHT)
    bricks.append(brick1)
    brick2 = Actor()
    brick2.set_position(Point(100, 10))
    brick2.set_image(constants.IMAGE_BRICK)
    brick2.set_width(constants.BRICK_WIDTH)
    brick2.set_height(constants.BRICK_HEIGHT)
    bricks.append(brick2)
    brick3 = Actor()
    brick3.set_position(Point(200, 10))
    brick3.set_image(constants.IMAGE_BRICK)
    brick3.set_width(constants.BRICK_WIDTH)
    brick3.set_height(constants.BRICK_HEIGHT)
    bricks.append(brick3)
    

    
    cast["bricks"] = bricks

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = []
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
