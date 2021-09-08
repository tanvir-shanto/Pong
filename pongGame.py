import turtle

import window
from paddles import paddle1, paddle2


ball = turtle.Turtle()    # The ball

def create_ball():
    ball.speed(0)
    ball.shape("circle")
    ball.color("yellow")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.25
    ball.dy = 0.25


create_ball()

# Functions which move the pedals
def paddle1_up():
    y = paddle1.ycor()
    y += 25
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 25
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 25
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 25
    paddle2.sety(y)


def check_keys():
    # Key management
    window.win.listen()  # Listens if any key has been pressed
    window.win.onkeypress(paddle1_up, 'w')
    window.win.onkeypress(paddle1_down, 's')
    window.win.onkeypress(paddle2_up, 'Up')
    window.win.onkeypress(paddle2_down, 'Down')


def check_collisions():
    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.dx *= -1
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() < -340) and (ball.ycor() < paddle1.ycor() + 50) and (ball.ycor() > paddle1.ycor() - 50):
        ball.dx *= -1
    elif (ball.xcor() > 340) and (ball.ycor() < paddle2.ycor() + 50) and (ball.ycor() > paddle2.ycor() - 50):
        ball.dx *= -1



# Game Loop
while True:
    window.win.update()
    check_keys()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    check_collisions()
