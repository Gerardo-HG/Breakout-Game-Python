from turtle import *


class Scoreboard(Turtle):
    """
    A class to manage the scoreboard for a game using the Turtle module.

    The scoreboard displays the player's score and remaining lives. It also handles game-winning
    and game-over messages.

    Attributes:
        points (int): The player's current score.
        lives (int): The player's remaining lives.
    """

    def __init__(self):
        """
        Initializes a Scoreboard instance.

        Behavior:
            - Sets up the turtle to display text (hidden turtle, no drawing).
            - Initializes the score (`points`) to 0 and lives to 5.
            - Calls the `update_scoreboard` method to display the initial score and lives.
        """
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.points = 0
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the current display and updates it with the latest score and lives.

        The scoreboard is positioned at the top-right corner of the screen (x=400, y=350).
        The text is aligned to the center and uses the Arial font, size 20, bold.
        """
        self.clear()
        self.goto(400, 350)
        self.write(f"Score:  {self.points}  |  Lives:  {self.lives}", align="Center", font=('Arial', 20, 'bold'))

    def hit_block(self):
        """
        Updates the score when a block is hit.

        Behavior:
            - Increments the `points` attribute by 7.
            - Calls `update_scoreboard` to reflect the new score.
        """
        self.points += 7
        self.update_scoreboard()

    def ball_fail(self):
        """
        Updates the scoreboard when the ball is missed.

        Behavior:
            - Decrements the `lives` attribute by 1.
            - Calls `update_scoreboard` to reflect the new number of lives.
        """
        self.lives -= 1
        self.update_scoreboard()

    def game_won(self):
        """
        Displays a game-winning message on the screen.

        Behavior:
            - Clears the current scoreboard.
            - Writes "CONGRATS YOU WON!" in the center of the screen, using Arial font, size 40, bold.
        """
        self.clear()
        self.goto(0, 0)
        self.write('CONGRATS YOU WON!', align="Center", font=('Arial', 40, 'bold'))

    def game_over(self):
        """
        Displays a game-over message on the screen.

        Behavior:
            - Clears the current scoreboard.
            - Writes "GAME OVER" in the center of the screen, using Arial font, size 40, bold.
        """
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', align="Center", font=('Arial', 40, 'bold'))
