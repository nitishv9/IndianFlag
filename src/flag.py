import turtle
from src.util import draw

#Turtle speed and pen size configuration
flag = turtle.Turtle()
turtle.speed(3)
turtle.pensize(5)


#Set Ashok Chakra color
flag.color("#054187")

#Draw Ashok Chakra
for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)
draw(flag,0, -80)
flag.circle( 80, 360)

#Draw green triangle
flag.color("green")
flag.begin_fill()
flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.end_fill()

#Draw Orange Triangle
flag.color("orange")
draw(flag,-350, 80)
flag.begin_fill()
flag.right(180)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.end_fill()

#Tear Down
flag.hideturtle()
turtle.done()