import turtle as t
from turtle import Turtle, Screen



for _ in range(4):
    t.pendown()
    t.forward(100)
    t.penup()
    t.forward(100)
    t.right(90)

screen = Screen()
screen.exitonclick()