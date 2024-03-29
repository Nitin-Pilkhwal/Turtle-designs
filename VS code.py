
import turtle as tr

def create(pen,a,b):
    pen.pencolor("blue")
    pen.fillcolor("blue")
    pen.penup()
    pen.goto(a,b)
    pen.pendown()
    pen.begin_fill()
    pen.right(-135)
    pen.forward(200)
    pen.right(-90)
    pen.forward(40)
    pen.right(-90)
    pen.forward(240)
    pen.right(-135)
    pen.forward(240)
    pen.right(125)
    pen.forward(80)
    pen.right(55)
    pen.forward(150)
    pen.right(54)
    pen.forward(80)
    pen.right(126)
    pen.forward(240)
    pen.right(-135)
    pen.forward(240)
    pen.right(-90)
    pen.forward(40)
    pen.right(-90)
    pen.forward(200)
    pen.end_fill()
    pen.right(45)
    pen.penup()

if __name__ == '__main__':
    screen=tr.Screen()
    screen.bgcolor("black")

    code1=tr.Turtle()
    code2=tr.Turtle()

    code1.pensize(3)
    code2.pensize(3)
    
    code1.speed(5)
    code2.speed(5)

    code1.hideturtle()
    code2.hideturtle()
    create(code1,0,0)
screen.mainloop()
