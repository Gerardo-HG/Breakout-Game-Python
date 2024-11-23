from turtle import *


class Paddle(Turtle):
    """
    A class to create and manage a paddle object for a game using the Turtle module.

    The paddle can move horizontally (left and right) and is designed for use in games like Pong.

    Attributes:
        position (tuple): The initial (x, y) coordinates of the paddle.
    """

    def __init__(self, position):
        """
        Initializes a Paddle instance at a specified position.

        Args:
            position (tuple): The initial (x, y) coordinates of the paddle.

        Behavior:
            - The paddle is created with a rectangular shape, orange color, and a vertical orientation.
            - The paddle's size is stretched vertically (`stretch_wid=15`) and minimally stretched horizontally (`stretch_len=1`).
            - The paddle is placed at the given position.
        """
        super().__init__()
        self.shape('square')
        self.color('orange')
        self.penup()
        self.right(90)  # Orients the paddle vertically.
        self.shapesize(stretch_wid=15, stretch_len=1)
        self.goto(position)

    def move_left(self):
        """
        Moves the paddle to the left by 100 units along the x-axis.

        The paddle's x-coordinate is decreased by 100 while the y-coordinate remains unchanged.
        """
        new_x = self.xcor() - 100
        self.goto(new_x, self.ycor())

    def move_right(self):
        """
        Moves the paddle to the right by 100 units along the x-axis.

        The paddle's x-coordinate is increased by 100 while the y-coordinate remains unchanged.
        """
        new_x = self.xcor() + 100
        self.goto(new_x, self.ycor())


