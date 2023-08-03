import turtle

gameplayscreen = turtle.Screen()
gameplayscreen.title("2 player ping Pong")
gameplayscreen.bgcolor("white")
gameplayscreen.setup(width=400, height=400)

"""left paddle"""
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

"""right paddle"""
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(+400, 0)

"""ball"""
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

"""player1/left player"""
player1 = 0

"""player2/right player"""
player2 = 0

"""score_board"""
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("dark blue")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 200)
score_board.write("player1 score = 0, player2 score = 0",align="center", font=("courier", 24, "normal"))


def left_paddle_up():
  y = left_paddle.ycor()
  y = y + 20
  if y > 200:
    y = 200
  left_paddle.sety(y)


def left_paddle_down():
  y = left_paddle.ycor()
  y = y - 20
  if y < -200:
    y = -200
  left_paddle.sety(y)


def right_paddle_up():
  y = right_paddle.ycor()
  y = y + 20
  if y > 200:
    y = 200
  right_paddle.sety(y)


def right_paddle_down():
  y = right_paddle.ycor()
  y = y - 20
  if y < -200:
    y = -200
  right_paddle.sety(y)



"""keyboard attach"""
gameplayscreen.listen()
gameplayscreen.onkey(left_paddle_up, "W")
gameplayscreen.onkey(left_paddle_down, "S")
gameplayscreen.onkey(right_paddle_up, "Up")
gameplayscreen.onkey(right_paddle_down, "Down")
while True:
  gameplayscreen.update()
  hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
  hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

  """ballborders"""
  #topborder
  if hit_ball.ycor() > 200:
    hit_ball.sety(200)
    hit_ball.dy = hit_ball.dy * (-1)

  #bottomborder
  if hit_ball.ycor() < -200:
    hit_ball.sety(-200)
    hit_ball.dy = hit_ball.dy * (-1)

  #rightborder
  if hit_ball.xcor() > 400:
    hit_ball.goto(0, 0)
    hit_ball.dx = hit_ball.dx * (-1)
    player1 = player1 + 1
    score_board.clear()
    score_board.write("player1 score = {}, player2 score = {}".format(player1, player2), align="center", font=("courier", 24, "normal"))
  #leftborder
  if hit_ball.xcor() < -400:
    hit_ball.goto(0, 0)
    hit_ball.dx = hit_ball.dx * (-1)
    player2 = player2 + 1
    score_board.clear()
    score_board.write("player1 score = {}, player2 score = {}".format(player1, player2), align="center", font=("courier", 24, "normal"))
    
#paddle ball collision
  if (hit_ball.xcor() > 380 and hit_ball.xcor() < 400) and ( hit_ball.ycor() < right_paddle.ycor() + 40 and hit_ball.ycor() > right_paddle.ycor() - 40):
    hit_ball.setx(380)
    hit_ball.dx = hit_ball.dx * (-1)
    
#paddle ball collision2
  if (hit_ball.xcor() < -380 and hit_ball.xcor() > -400) and ( hit_ball.ycor() < left_paddle.ycor() + 40 and hit_ball.ycor() > left_paddle.ycor() - 40):
    hit_ball.setx(-380)
    hit_ball.dx = hit_ball.dx * (-1)

#Game Winning
  if player1 == 2:
    score_board.clear()
    score_board.write("player1 won the game but no one cares:)", align="center", font=("courier", 24, "bold"))

    player1 = 0
    player2 = 0
    break
  if player2 == 2:
    score_board.clear()
    score_board.write("player2 won the game but no one cares:)", align="center", font=("courier", 24, "bold"))
    player1 = 0
    player2 = 0
    break
