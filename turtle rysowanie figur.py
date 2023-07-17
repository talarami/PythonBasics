import turtle
# KWADRAT: 

t1 = turtle.Turtle()
t1.pensize(10)
t1.color("green")
t1.fillcolor("yellow") # wypełnienie figury kolorem
t1.penup() # podniesienie pisaka
t1.goto(-300, 300) # wybór pozycji; punkt 0,0 jest w środku ekranu; oś X idzie dodatnio w prawo, a oś Y idzie dodatnio w górę
t1.pendown() # odłozenie pisaka

t1.begin_fill() # rozpoczęcie wypełniania
for i in range(4): # 4 wartości
    t1.forward(80) # 80 jednostek prosto
    t1.right(90) # skręt 90 stopni w prawo
t1.end_fill() # dzięki temu figura będzie wypełniona

# TRÓJKĄT

t1.fillcolor("blue")
t1.penup()
t1.goto(-200, -250)
t1.pendown()

t1.begin_fill()
for i in range(3):
    t1.forward(80)
    t1.right(120)
t1.end_fill()

# OKRĄG 

t2 = turtle.Turtle()
t2.width(10)
t2.fillcolor("red")
t2.color("purple")
t2.penup()
t2.goto(300, 200)
t2.pendown()

t2.begin_fill()
t2.circle(70) # okrąg
t2.end_fill()

# KILKA OKRĘGÓW PRZENIKAJĄCYCH SIĘ

t3 = turtle.Turtle()
t3.width(4)
t3.color("green")
t3.penup()
t3.goto(0,0)
t3.pendown()
t3.speed(55) # szybkość malowania

for i in range(200):
    t3.circle(110)
    t3.left(8)


turtle.mainloop()