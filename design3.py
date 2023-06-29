import turtle
def square(t_turtle):
    for i in range(1,5):
        t_turtle.forward(200)
        t_turtle.right(90)

def design():
    bg = turtle.Screen()
    bg.bgcolor('purple')
    #Turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(18)
    brad.pensize(3)
    for i in range(1,37):
        square(brad)
        brad.right(10)

    window.exitonclick()

design()
