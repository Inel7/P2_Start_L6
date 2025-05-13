import turtle
import random


class TurtleRacer:
    def __init__(self,color,index):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto((-200, 200 - (index * 30)))
        self.turtle.pendown()

    def race (self):
        random_afstand = random.randint(1, 25)
        self.turtle.forward(random_afstand)

    def dance(self):
        self.turtle.left(360)
        self.turtle.right(360)

racers = [
    TurtleRacer("red", 1),
    TurtleRacer("blue", 2),
    TurtleRacer("green", 3)
]

for i in range(25):
    for racer in racers:
        racer.race()

for racer in racers:
    racer.dance()



turtle.done()