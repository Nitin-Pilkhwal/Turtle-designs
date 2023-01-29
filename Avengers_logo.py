import turtle as tr


screen=tr.Screen()
screen.bgcolor("black")


def create_outer_circle(avenger):
    avenger.setposition(80,12)
    avenger.pendown()
    avenger.pencolor("white")
    avenger.pensize(2)
    avenger.fillcolor("#581fe9")
    avenger.begin_fill()
    avenger.circle(152)
    avenger.end_fill()
    avenger.penup()


def create_inner_circle(avenger):
    avenger.pensize(2)
    avenger.pencolor("black")
    avenger.fillcolor("black")
    avenger.setposition(80,29)
    avenger.pendown()
    avenger.begin_fill()
    avenger.circle(135)
    avenger.end_fill()
    avenger.penup()


def create_A(avenger):
    avenger.goto(0,0)
    avenger.pendown()
    avenger.pensize(3)
    avenger.pencolor("white")
    avenger.fillcolor("#581fe9")
    avenger.begin_fill()
    avenger.forward(25)
    avenger.right(-60)
    avenger.forward(70)
    avenger.right(60)
    avenger.forward(50)
    avenger.right(90)
    avenger.forward(30)
    avenger.right(-90)
    avenger.forward(70)
    avenger.right(-90)
    avenger.forward(290)
    avenger.right(-90)
    avenger.forward(75)
    avenger.right(-60)
    avenger.forward(370)
    avenger.goto(0,0)
    avenger.end_fill()
    avenger.penup()


def create_gap(avenger):
    avenger.pendown()
    avenger.fillcolor("black")
    avenger.pencolor("white")
    avenger.begin_fill()
    avenger.penup()
    avenger.goto(71,88)
    avenger.pendown()
    avenger.right(240)
    avenger.forward(38)  #1
    avenger.right(-90)
    avenger.forward(90)  #2
    avenger.goto(71,88)
    avenger.end_fill()
    avenger.penup()


def arrow(avenger):
    avenger.pensize(3)
    avenger.goto(110,32)
    avenger.pendown()
    avenger.right(60)
    avenger.forward(80)
    avenger.goto(110,112)
    avenger.penup()

if __name__ == '__main__':
    avenger=tr.Turtle()
    avenger.color("red")
    # avenger.speed(20)
    avenger.hideturtle()
    avenger.penup()
    create_outer_circle(avenger)
    create_inner_circle(avenger)
    create_A(avenger)
    create_gap(avenger)
    arrow(avenger)

screen.mainloop()