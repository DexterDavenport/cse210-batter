# from game.action import Action
# from game import constants
# from game.point import Point


# class Handle_Off_Screen_Action(Action):
#     def __init__(self, physics_service):
#         super().__init__()
#         self._physics_service = physics_service

#     def execute(self, cast):
#         ball = cast["balls"][0]
#         bricks = cast["bricks"]
#         times_run = 0
#         for brick in bricks:
#             if self._physics_service.is_collision(ball, brick):
#                 x = 5
#                 y = 5
#                 ball.set_velocity(Point(x,y))
#                 times_run += 1
#                 print(times_run)








from game.point import Point
from game import constants
from game.action import Action



class Handle_Off_Screen_Action(Action):



    def execute(self, cast):

        ball = cast["balls"][0]

        # paddle = cast["paddles"][0]



        if ball.get_position().get_x() <= 1:
            print('left edge')
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
            
        if ball.get_position().get_x() >= 776:
            print('right edge')
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        if ball.get_position().get_y() <= 0:
            print('top edge')
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        if ball.get_position().get_y() >= 576:
            print('bottom edge')
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        

