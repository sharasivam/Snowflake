import turtle
from random import *

# initate turtle bernd
bernd = turtle.Turtle()
bernd.speed(0)

# snowflake colors to choose from
colors = ['blue', 'red', 'green', 'gold', 'purple', 'pink', 'cyan', 'black', 'CadetBlue3']

# generates random snowflake
def randflake(int):
    bernd.color(choice(colors))
    for i in range(12):
        for i in range(int):
            bernd.forward(60)
            bernd.right(120)
            bernd.forward(60)
            bernd.right(180)
        bernd.right(30)

# generates a perfect snowflake branch
def branch():
    count = 0
    while count < 3:
        count2 = 0
        while count2 < 3:
            bernd.forward(10)
            bernd.backward(10)
            bernd.right(45)
            count2 = count2 + 1
        bernd.left(90)
        bernd.backward(10)
        bernd.left(45)
        count = count + 1
    bernd.right(90)
    bernd.forward(30)
    
# generates a normal snowflake
def normflake():
    bernd.color(choice(colors))
    i = 0
    while i < 8:
        branch()
        bernd.left(45)
        i = i + 1
        
# moving pen to starting position
bernd.penup()
bernd.goto(100,200)
bernd.pendown()

# creating a mixture of snowflakes
for i in range(1):
#     randflake(randint(2,8))
#     bernd.penup()
#     bernd.right(76)
#     bernd.forward(200)
#     bernd.pendown()
    normflake()
    bernd.penup()
    bernd.right(60)
    bernd.forward(250)
    bernd.pendown()