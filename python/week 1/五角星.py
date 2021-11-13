import turtle
turtle.fillcolor("red")
turtle.begin_fill()
while True:
    turtle.forward(300)
    turtle.right(144)
    if abs(turtle.pos())<1:
        break
turtle.end_fill()