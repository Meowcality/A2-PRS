import turtle
import random

def pc():
    turtle.colormode(255)
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    turtle.pencolor(r, g, b)
pc()
turtle.bgcolor('Silver')
turtle.write("YOU WIN", align="center", font=("Monotype Corsiva", 160, "normal"))





       

        

