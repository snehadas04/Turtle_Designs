import turtle
import colorsys

turtle.bgcolor("black")
turtle.speed("fastest")
c=0.0
turtle.hideturtle()

for i in range(450):
    colors = colorsys.hsv_to_rgb(c,1,1)
    turtle.color(colors)
    c+=0.005