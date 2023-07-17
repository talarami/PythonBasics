import turtle

turtle.color("deep pink")
style = ("Courier", 20, "italic")
turtle.write("Hej Domisiu kocham Cie", font=style, align="left")
turtle.hideturtle()

t1 = turtle.Turtle()

def curve():
    t1.pen(pencolor="deep pink", pensize=3, speed=10)
    for i in range(200):
        t1.right(1)
        t1.forward(1)

def heart():
    t1.pen(pencolor="deep pink", fillcolor="deep pink", pensize=3, speed=1500)
    t1.shape("turtle")
    t1.shapesize(1,1,1)
    t1.penup()
    t1.goto(-300, 100)
    t1.pendown()
    t1.begin_fill()
    t1.right(230)
    t1.forward(113)
    curve()
    t1.lt(120)
    curve()
    t1.forward(112)
    t1.end_fill()

t1.hideturtle()

heart()

turtle.mainloop()