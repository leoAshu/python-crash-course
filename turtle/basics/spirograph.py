import random
from turtle import Turtle, Screen

ttl = Turtle()
ttl.speed('fastest')

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'SlateGray', 'SeaGreen']

size_of_gap = 5

for _ in range(360 // size_of_gap):
    ttl.color(random.choice(colors))
    ttl.circle(100)
    ttl.setheading(ttl.heading() + size_of_gap)

screen = Screen()
screen.exitonclick()