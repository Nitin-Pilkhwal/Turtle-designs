import turtle
import random 

spiral = turtle.Turtle()
colours = ["red", "blue", "black"]

for i in range(40):
    spiral.color(random.choice(colours))
    spiral.forward(i * 10)
    spiral.right(144)
turtle.done()