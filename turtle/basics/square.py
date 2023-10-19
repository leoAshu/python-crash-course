from turtle import Turtle, Screen

ttl = Turtle()
ttl.shape('turtle')
ttl.color('teal')

for _ in range(4):
    ttl.right(90)
    ttl.forward(100)


screen = Screen()
screen.exitonclick()