import turtle
turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(15)
squary.pencolor("red")
for i in range(500):
    squary.forward(i)
    squary.left(150)
    squary.pensize(1)