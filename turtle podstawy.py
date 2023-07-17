import turtle
import random

t = turtle.Turtle()

t.forward(100) # przejście o 100 jednostek
t.right(45) # obrót w prawo o 45 stopni
t.fd(50) # to samo co forward o 50 jednostek
t.left(90) # obrót w lewo o 90 stopni
t.backward(60) # przejście do tyłu o 60 jednostek
t.penup() # podniesienie wskaźnika żółwia

t.goto(0,0) # powrót do układu współrzędnych
t.pendown() # powrót do możliwości ponownego rysowania żółwiem

for i in range(25):
    t.color( random.choice(["red", "green", "blue", "yellow"]) ) # program wybierze losowy kolor żółwia
    t.width(i + 1) # grubość lini
    t.fd(80 + 20 * i) # przejście na przód
    t.right(90) # obrót

turtle.mainloop() # interfejs będzie widoczny po wyświetleniu programu