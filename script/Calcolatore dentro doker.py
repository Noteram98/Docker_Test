import turtle

# Impostazioni iniziali
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#0db7ed")

# Disegna il corpo della balena
def draw_body():
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#ffffff")
    turtle.circle(100)
    turtle.end_fill()

# Disegna la pinna della balena
def draw_fin():
    turtle.penup()
    turtle.goto(-25, -75)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(0, -125)
    turtle.goto(25, -75)
    turtle.goto(-25, -75)
    turtle.end_fill()

# Disegna l'occhio della balena
def draw_eye():
    turtle.penup()
    turtle.goto(-30, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#ffffff")
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-20, 40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#000000")
    turtle.circle(5)
    turtle.end_fill()

# Nasconde la freccia di Turtle
turtle.hideturtle()

# Disegna la balena
draw_body()
draw_fin()
draw_eye()

# Chiudi la finestra facendo clic
screen.exitonclick()

