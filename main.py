from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("pong")
    screen.tracer(0)

    left_paddle = Paddle()
    right_paddle = Paddle()
    left_paddle.setup_left()
    right_paddle.setup_right()
    ball = Ball()
    left_score = Scoreboard((-60, 210))
    right_score = Scoreboard((60, 210))
    screen.update()

    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        ball.move()
        if ball.xcor() > 380:
            left_score.update_score()
            ball.retry()
            screen.update()
            time.sleep(1.5)
        elif ball.xcor() < -390:
            right_score.update_score()
            ball.retry()
            screen.update()
            time.sleep(1.5)
        elif ball.distance(right_paddle) < 50 and ball.xcor() > 330 or \
                ball.distance(left_paddle) < 50 and ball.xcor() < -300:
            ball.reverse()
        elif ball.ycor() >= 290 or ball.ycor() <= -280:
            ball.bounce()
        time.sleep(ball.move_speed)
        screen.update()



    screen.exitonclick()

