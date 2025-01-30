import turtle
import random

len = 40
def shape():
    for i in range(8):
        '''
        turtle.fillcolor(random.random(0.0, 255.0), random.random(0.0,255.0), random.random(0.0,255.0))
        Anche se inserisco dei numeri che non usano il random, mi dà errore ("bad color sequence")
        '''
        turtle.forward(len)
        turtle.right(45)
def block():
    for i in range(18):
        shape()
        turtle.right(20)
    
def riga():
    block()
    turtle.penup()
    turtle.forward(len*10)
    turtle.pendown()
    block()

def mattonella():
    riga()
    turtle.penup()
    turtle.goto(-200,-180)
    turtle.pendown()
    riga()

turtle.speed(8)
turtle.penup()
turtle.goto(-200,180)
turtle.pendown()
mattonella()

wait = input()

