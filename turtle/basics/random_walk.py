import random
from turtle import Turtle, Screen

ttl = Turtle()
ttl.shape('turtle')
ttl.pensize(15)
ttl.speed('fastest')

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'SlateGray', 'SeaGreen']
direction = [0, 90, 180, 270]

for _ in range(200):
    ttl.color(random.choice(colors))
    ttl.forward(30)
    ttl.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()