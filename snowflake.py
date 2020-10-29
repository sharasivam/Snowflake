import turtle
from random import randint

bernd = turtle.Turtle()
bernd.speed(0)


def randflake(flakeno):
    for i in range(12):
        for i in range(flakeno):
            bernd.forward(60)
            bernd.right(120)
            bernd.forward(60)
            bernd.right(180)
        bernd.right(30)
       

    randflake(randint(2,8))
    bernd.penup()
    bernd.right(76)
    bernd.forward(150)
    bernd.down()
    randflake(randint(2,8))