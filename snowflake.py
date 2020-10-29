import turtle
from random import *

# initate turtle bernd
bernd = turtle.Turtle()
bernd.speed(0)

# snowflake colors to choose from
colors = ['blue', 'red', 'green', 'gold', 'purple', 'black', 'cyan', 'lavender', 'CadetBlue3']

# generates random snowflake
def randflake(flakeno):
    bernd.color(choice(colors))
    for i in range(12):
        for i in range(flakeno):
            bernd.forward(60)
            bernd.right(120)
            bernd.forward(60)
            bernd.right(180)
        bernd.right(30)

# generates a perfect snowflake branch
def branch():
    for i in range(3):
        for i in range(3):
            bernd.forward(10)
            bernd.backward(10)
            bernd.right(45)
        bernd.left(90)
        bernd.backward(10)
        bernd.left(45)
    bernd.right(90)
    bernd.forward(30)
    
# generates a normal snowflake
def normflake():
    bernd.color(choice(colors))
    for i in range(8):
        branch()
        bernd.left(45)
        
# moving pen to starting position
bernd.penup()
bernd.goto(100,200)
bernd.pendown()

# creating a mixture of snowflakes
for i in range(5):
    randflake(randint(2,8))
    bernd.penup()
    bernd.right(76)
    bernd.forward(200)
    bernd.pendown()
    normflake()
    bernd.penup()
    bernd.right(54)
    bernd.forward(250)
    bernd.pendown()