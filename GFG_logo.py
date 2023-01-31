# importing turtle for graphics
import turtle

tut = turtle.Screen()
tut.bgcolor("White")
pen = turtle.Turtle()
pen.speed(1)
pen.color("Green")
pen.width(10)
pen.up()
pen.goto(-18,18)
pen.down()
tut = turtle.Screen()
for x in range(180):
    pen.forward(1)
    pen.right(1)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(130)
pen.right(90)
pen.forward(50)
pen.left(90)
for x in range(180):
    pen.backward(1)
    pen.right(1)
turtle.done()
