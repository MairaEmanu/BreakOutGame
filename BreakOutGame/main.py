#TODO: Points for the bricks


from paddle import Paddle
from turtle import Screen
from ball import Ball
from brick import Bricks
from scoreboard import Scoreboard
import time

#------ CONSTANTS------#

BACKGROUND = "#424874"

# WALLS
LEFT_WALL = -370
RIGHT_WALL = 370
UPPER_WALL = 270

# ------- SCREEN SETUP ------------------#
screen = Screen()
screen.bgcolor(BACKGROUND)
screen.setup(height=700, width=800)
screen.title("BreakOut")
screen.tracer(0)


# ----------- COMPONENTS INITIATION ---------#
paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()



screen.update()

# -------------- GET USER'S INPUT ----------#
screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")


#----------------- START GAME ---------------#
game_on = True
start_ball = True

while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()


    # Detect collision with walls:
    if ball.xcor() > RIGHT_WALL or ball.xcor() < LEFT_WALL:
        ball.bounce_x()

    # Detect collision with upper wall:
    if ball.ycor() > UPPER_WALL:
        ball.bounce_y()


   # detect collision with brick
    for brick in bricks.bricks:
        if ball.distance(brick) < 49:
            if ball.ycor() < brick.upper:
                ball.bounce_y()
            elif ball.ycor() < brick.bottom:
                ball.bounce_y()
            elif ball.xcor() < brick.right:
                ball.bounce_x()
            elif ball.xcor() < brick.left:
                ball.bounce_x()
            brick.remove()



    # Detect missed collision with paddle
    if ball.ycor() < -275:
        ball.miss()
        paddle.missed_ball()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_on = False
        else:
            scoreboard.decrease_lives()
        time.sleep(1)

    # Detect collision with paddle:
    if ball.ycor() < -230 and paddle.distance(ball) < 50:
        ball.bounce_y()






screen.exitonclick()
