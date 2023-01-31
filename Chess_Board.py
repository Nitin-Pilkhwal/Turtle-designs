import turtle

sc = turtle.Screen()
cb = turtle.Turtle()
def draw():
    for i in range(4):
        cb.forward(30)
        cb.left(90)
    cb.forward(30)
if __name__ == "__main__":
    sc.setup(400, 600)
    cb.speed(100)
    for i in range(8):
        cb.up()
        cb.setpos(-100, 30 * i)
        cb.down()
        for j in range(8):
            if (i + j) % 2 == 0:
                col = 'black'
            else:
                col = 'white'
            cb.fillcolor(col)
            cb.begin_fill()
            draw()
            cb.end_fill()
    cb.hideturtle()
    turtle.done()
