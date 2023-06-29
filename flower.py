from turtle import *
bgcolor('black')
speed(16)
col=['pink','green','yellow','red','blue','orange']

for i in range(60):
    pencolor(col[i%6])
    pensize(2)
    circle(190-i/3,90)
    left(90)
    circle(190-i/3,90)
    left(60)