from turtle import *
import random as rd


class Ball(Turtle):
    """
    A class to create and manage a ball object for a game using the Turtle module.

    The ball moves in a 2D plane, can bounce off surfaces, and can reset its position.

    Attributes:
        x_move (int): Horizontal speed of the ball.
        y_move (int): Vertical speed of the ball.
    """

    def __init__(self, position):
        """
        Initializes a Ball instance at a specified position.

        Args:
            position (tuple): The initial (x, y) coordinates of the ball.

        Behavior:
            - The ball is created with a circular shape, blue color, and a size of 1x1.
            - The ball starts with an initial movement speed of 3 units in both x and y directions.
            - The ball is placed at the given position.
        """
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.x_move = 3
        self.y_move = 3
        self.speed(0.1)
        self.goto(position)

    def move(self):
        """
        Updates the position of the ball based on its current speed.

        The ball's new position is calculated by adding its `x_move` and `y_move` values
        to its current coordinates.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the vertical direction of the ball's movement.

        Multiplies `y_move` by -1, simulating a bounce on the horizontal axis (e.g., floor or ceiling).
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the horizontal direction of the ball's movement.

        Multiplies `x_move` by -1, simulating a bounce on the vertical axis (e.g., wall or paddle).
        """
        self.x_move *= -1

    def reset_ball(self):
        """
        Resets the ball's position to the center of the screen and sets its starting vertical position.

        The ball is moved to coordinates `(0, -200)`, typically for restarting a game or after scoring.
        """
        self.goto((0, -200))

