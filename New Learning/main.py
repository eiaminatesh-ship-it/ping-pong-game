import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)  # Turns off automatic screen updates for smooth performance

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(0)  # Fast draw speed
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
left_player = 0
right_player = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

# Functions to move paddles (Adjusted limits to keep paddles inside the screen)
def paddleaup():
    y = left_pad.ycor()
    if y < 240:  
        y += 20
        left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    if y > -240:  
        y -= 20
        left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    if y < 240:  
        y += 20
        right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  
        y -= 20
        right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")  
sc.onkeypress(paddleadown, "s")  
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Main game loop
while True:
    sc.update()
    time.sleep(0.01)  # Limits frame rate for consistent speed

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking borders (Top/Bottom bounce)
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    # Right side score limit
    if hit_ball.xcor() > 490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1  # Reverse horizontal direction to serve to the other side
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Left side score limit
    if hit_ball.xcor() < -490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1  # Reverse horizontal direction to serve to the other side
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Accurate paddle-ball collision
    # Right paddle: center x=400, left edge is 380. Ball radius is 10.
    if (370 <= hit_ball.xcor() <= 385) and \
       (right_pad.ycor() - 70 <= hit_ball.ycor() <= right_pad.ycor() + 70):
        hit_ball.setx(370)
        hit_ball.dx *= -1

    # Left paddle: center x=-400, right edge is -380. Ball radius is 10.
    if (-385 <= hit_ball.xcor() <= -370) and \
       (left_pad.ycor() - 70 <= hit_ball.ycor() <= left_pad.ycor() + 70):
        hit_ball.setx(-370)
        hit_ball.dx *= -1