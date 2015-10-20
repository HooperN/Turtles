import turtle
screen = turtle.Screen()
nick = turtle.Turtle()

def boombox(jim):
    jim.shape("turtle")
    jim.pendown()
    jim.forward(100)
    jim.penup()
    jim.left(90)
    jim.forward(50)
    jim.write("Hi")
    jim.back(20)
    lol = input()

boombox(nick)
fin = input()

