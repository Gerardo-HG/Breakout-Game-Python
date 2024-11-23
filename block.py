from turtle import *
import random as rd

# Constants
COLORS = ["red", "green", "white", "yellow", "blue", "pink", "brown", "purple", "orange"]
BLOCK_POSITIONS = [(-400, 300), (-250, 300), (-100, 300), (50, 300), (200, 300), (350, 300), (450, 300),
                   (-400, 200), (-250, 200), (-100, 200), (50, 200), (200, 200), (350, 200), (450, 200),
                   (-400, 100), (-250, 100), (-100, 100), (50, 100), (200, 100), (350, 100), (450, 190),
                   (-400, 0), (-250, 0), (-100, 0), (50, 0), (200, 0), (350, 0), (450, 0)]


class Block(Turtle):
    """
    A class to create and manage a collection of square-shaped turtle blocks.

    Attributes:
        blocks (list): A list to store all the turtle blocks created.

    Methods:
        __init__(): Initializes the Block instance and creates the blocks.
        draw_blocks(): Creates blocks at specified positions with random colors and sizes.
        delete_block(block_detected): Removes a block from the list and moves it off-screen.
    """

    def __init__(self):
        """
        Initializes the Block instance.
        Creates an empty list to store the blocks and calls the draw_blocks method
        to populate the screen with blocks.
        """
        super().__init__()
        self.blocks = []
        self.draw_blocks()

    def draw_blocks(self):
        """
        Creates turtle blocks at predefined positions with random colors and sizes.

        For each position in BLOCK_POSITIONS, a turtle block is created:
        - Shape: Square
        - Color: Randomly chosen from COLORS
        - Size: Randomly set with a width of 3 and a length between 3 and 4
        - Position: Set according to the BLOCK_POSITIONS list
        The block is then added to the `blocks` list for tracking.
        """
        for i in range(len(BLOCK_POSITIONS) - 1):
            new_block = Turtle('square')
            new_block.color(rd.choice(COLORS))
            new_block.penup()
            block_length = rd.randint(3, 4)
            new_block.turtlesize(stretch_wid=3, stretch_len=block_length)
            new_block.goto(BLOCK_POSITIONS[i])
            self.blocks.append(new_block)

    def delete_block(self, block_detected):
        """
        Removes a block from the `blocks` list and moves it off-screen.

        Args:
            block_detected (Turtle): The block to be removed.

        Behavior:
            - If the block is found in the list, it is moved to coordinates (2000, 2000)
              and removed from the list.
        """
        if block_detected in self.blocks:
            block_detected.goto(2000, 2000)
            self.blocks.remove(block_detected)
