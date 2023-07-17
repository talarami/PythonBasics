
import turtle
import time # pozwoli na wstrzymanie programu na określony czas

t = turtle.Turtle()
win = turtle.Screen() # uchwyt do ekranu
win.bgcolor("yellow") # w praktyce żółty bg
win.setup(width=600, height=600) # wymiary ekranu

t.forward(80)
print("x:", t.xcor())
print("y:", t.ycor())

def keyPressedW():
    print("w clicked")
    t.fd(20)

def keyPressedS():
    print("s clicked")
    t.backward(20)

def keyPressedA():
    print("a clicked")
    t.left(20)

def keyPressedD():
    print("d clicked")
    t.right(20)


win.listen()  # podpięcie funkcji do odpowiednich klawiszy
win.onkey( keyPressedW, "w" )
win.onkey( keyPressedS, "s" )
win.onkey( keyPressedA, "a" )
win.onkey( keyPressedD, "d" )

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1) # usypianie programu w każdej klatce na 0.1 sekundy

   

