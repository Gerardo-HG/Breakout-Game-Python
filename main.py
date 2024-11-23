from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1100,height=800)
screen.title("Break Point")
screen.tracer(0)

horizontal_bar = Paddle((0,-320))
ball = Ball((0,-200))

score = Scoreboard()

block = Block()

screen.listen()
screen.onkey(key='Right',fun=horizontal_bar.move_right)
screen.onkey(key='Left',fun=horizontal_bar.move_left)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Check if there are no more lives to play
    if score.lives == 0:
        score.game_over()
        game_is_on = False

    # Detect if all the blocks had been removed
    if len(block.blocks) == 0:
        score.game_won()
        game_is_on = False

    # Detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Detect collision with wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with the horizontal paddle
    if horizontal_bar.distance(ball) < 45 and ball.ycor() > -380:
        ball.bounce_y()

    # Detect if the ball misses the paddle
    if ball.ycor() < -380:
        score.ball_fail()
        ball.reset_ball()

    for b in block.blocks:
        if ball.distance(b) < 45:
            ball.bounce_y()
            score.hit_block()
            block.delete_block(b)

screen.exitonclick()