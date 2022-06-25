import turtle

wn = turtle.Screen()
wn.title("Tel-U PingPong")
wn.bgcolor("white")
wn.setup(width=600, height=800)
wn.tracer(0)

#Skor
skor_A = 0
skor_B = 0

#Stick_1
stick_1 = turtle.Turtle()
stick_1.speed(0)
stick_1.shape("square")
stick_1.color("black")
stick_1.shapesize(stretch_wid=1, stretch_len=7)
stick_1.penup()
stick_1.goto(0,-350)

#Stick_2
stick_2 = turtle.Turtle()
stick_2.speed(0)
stick_2.shape("square")
stick_2.color("black")
stick_2.shapesize(stretch_wid=1, stretch_len=7)
stick_2.penup()
stick_2.goto(0,350)

#Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("green")
bola.shapesize(stretch_wid=1, stretch_len=1)
bola.penup()
bola.goto(0,0)
bola.dx = 1 
bola.dy = 1 

#Papan Skor
papan = turtle.Turtle()
papan.speed (0)
papan.color("black")
papan.penup()
papan.hideturtle()
papan.goto(0,0)
papan.write("Player A: 0 \nPlayer B: 0", align="center", font=("Courier",24, "normal"))


#Fungsi
try: 
    def stick_1_kanan():
        x = stick_1.xcor()
        x += 20
        stick_1.setx(x)
        if x > 340:
            raise IOError("Lewat batas")

    def stick_1_kiri():
        x = stick_1.xcor()
        x += -20
        stick_1.setx(x)
        if x < -340:
            raise IOError("Lewat batas")

    def stick_2_kanan():
        x = stick_2.xcor()
        x += 20
        stick_2.setx(x)
        if x > 340:
            raise IOError("Lewat batas")

    def stick_2_kiri():
        x = stick_2.xcor()
        x += -20
        stick_2.setx(x)
        if x < -340:
            raise IOError("Lewat batas")

except:
    pass

#Kursor Keyboard
wn.listen()
wn.onkeypress (stick_1_kanan,"Right")
wn.onkeypress (stick_1_kiri,"Left")
wn.onkeypress (stick_2_kanan,"s")
wn.onkeypress (stick_2_kiri,"a")

while True:
    wn.update()

    #Gerak bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #Batas
    if bola.ycor() > 350:
        bola.goto(0, 0)
        bola.dy *= -1
        skor_B += 1
        papan.clear()
        papan.write("Player A: {} \nPlayer B: {}".format(skor_A, skor_B), align="center", font=("Courier",24, "normal"))


        if skor_B == 5:
            papan.clear()
            papan.write("Player B is the winner!!!", align="center", font=("Courier",24, "normal"))
            bola.goto(0,-10)
            bola.dx = 0
            bola.dy = 0
    
    if bola.ycor() < -350:
        bola.goto(0, 0)
        bola.dy *= -1
        skor_A += 1
        papan.clear()
        papan.write("Player A: {} \nPlayer B: {}".format(skor_A, skor_B), align="center", font=("Courier",24, "normal"))


        if skor_A == 5:
            papan.clear()
            papan.write("Player A is the winner!!!", align="center", font=("Courier",24, "normal"))
            bola.goto(0,-10)
            bola.dx = 0
            bola.dy = 0
    
    
    if bola.xcor() > 290:
        bola.setx(290)
        bola.dx *= -1
    
    if bola.xcor() < -290:
        bola.sety(-290)
        bola.dx *= -1
    
    #Gerak Stick
    if (bola.ycor() < -340 and bola.ycor() > -350) and (bola.xcor() < stick_1.xcor() + 40 and bola.xcor() > stick_1.xcor() -40):
        bola.sety(-340)
        bola.dy *= -1

    if (bola.ycor() > 340 and bola.ycor() < 350) and (bola.xcor() < stick_2.xcor() + 40 and bola.xcor() > stick_2.xcor() -40):
        bola.sety(340)
        bola.dy *= -1