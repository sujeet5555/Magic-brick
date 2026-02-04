import turtle

screen = turtle.Screen()
screen.title("Magic bricks")
screen.setup(800, 700)
screen.bgcolor("#87CEEB")

bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()

bg.goto(-400, -350)
bg.color("#228B22")
bg.begin_fill()
for _ in range(2):
    bg.forward(800)
    bg.left(90)
    bg.forward(200)
    bg.left(90)
bg.end_fill()

bg.goto(-350, -300)
bg.color("white")
bg.pensize(3)
bg.pendown()
for _ in range(2):
    bg.forward(700)
    bg.left(90)
    bg.forward(600)
    bg.left(90)
bg.penup()

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -260)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)

ball_dx = 4
ball_dy = 4

bricks = []
colors = ["#FF6347", "#FFD700", "#1E90FF"]

y = 180
for row in range(3):
    for x in range(-250, 251, 100):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)
    y -= 40

score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("black")
score_pen.penup()
score_pen.goto(-370, 310)
score_pen.write("Score: 0", font=("Arial", 14, "bold"))

msg = turtle.Turtle()
msg.hideturtle()
msg.color("black")
msg.penup()
msg.goto(0, 0)

button = turtle.Turtle()
button.shape("square")
button.color("#FFA500")
button.shapesize(stretch_wid=2, stretch_len=6)
button.penup()
button.goto(0, -40)
button.hideturtle()

btn_text = turtle.Turtle()
btn_text.hideturtle()
btn_text.penup()

def move_left():
    global ball_dy
    if ball_dy < 0:
        paddle.setx(paddle.xcor() - 40)

def move_right():
    global ball_dy
    if ball_dy < 0:
        paddle.setx(paddle.xcor() + 40)

def show_retry():
    button.showturtle()
    btn_text.goto(-55, -55)
    btn_text.write("TRY AGAIN", font=("Arial", 12, "bold"))

def reset_game():
    global score, ball_dx, ball_dy
    msg.clear()
    btn_text.clear()
    button.hideturtle()
    score = 0
    score_pen.clear()
    score_pen.write("Score: 0", font=("Arial", 14, "bold"))
    ball.goto(0, -230)
    ball_dx = 4
    ball_dy = 4
    for brick in bricks:
        brick.showturtle()
    game_loop()

def check_win():
    for brick in bricks:
        if brick.isvisible():
            return False
    return True

def game_loop():
    global ball_dx, ball_dy, score
    while True:
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        if ball.xcor() > 340 or ball.xcor() < -340:
            ball_dx *= -1

        if ball.ycor() > 290:
            ball_dy *= -1

        if ball.distance(paddle) < 60 and ball.ycor() < -230:
            ball_dy *= -1

        for brick in bricks:
            if brick.isvisible() and ball.distance(brick) < 50:
                brick.hideturtle()
                ball_dy *= -1
                score += 10
                score_pen.clear()
                score_pen.write(f"Score: {score}", font=("Arial", 14, "bold"))
                break

        if check_win():
            msg.write("🎉 YOU WON! 🎉", align="center", font=("Arial", 24, "bold"))
            show_retry()
            return

        if ball.ycor() < -330:
            msg.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            show_retry()
            return

def retry_click(x, y):
    if -90 < x < 90 and -80 < y < 0:
        reset_game()

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onclick(retry_click)

reset_game()
screen.mainloop()
