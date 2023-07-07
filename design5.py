import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("navy")
t.width(2)
t.speed(15)
col = ('white','pink','cyan')
for i in range(120):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)