import turtle as t
t.Screen().bgcolor("Black")
t.speed(15)
t.begin_fill()
t.fillcolor('#1DB954')
t.pencolor("#1DB954")
t.pensize(0)
t.circle(100)
t.end_fill()
t.penup()
t.goto(40,50)
t.pendown()
t.left(150)
t.forward(0)
t.pensize(15)
t.pencolor('black')
t.circle(80,60)
t.penup()

t.goto(50,85)
t.pendown()
t.pensize(17)
t.right(60)
t.forward(0)
t.circle(100,60)

t.penup()
t.goto(60,120)
t.pendown()
t.pensize(20)
t.right(60)
t.forward(0)
t.circle(120,60)

t.penup()
t.goto(-115, -115)
t.pendown()
t.color("#1DB954")
t.write("Spotify", font=("Arial", 60, "bold"))

t.done()