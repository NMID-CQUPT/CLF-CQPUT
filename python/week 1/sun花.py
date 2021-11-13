import turtle
turtle.pensize(5)
turtle.color("red","yellow")
turtle.begin_fill()
while True:
    turtle.forward(300)
    turtle.left(175)
    if abs(turtle.pos())<1:
        break
turtle.end_fill()  