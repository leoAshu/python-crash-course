from turtle import Turtle, Screen

ttl = Turtle()
ttl.shape('turtle')
ttl.color('teal')

for _ in range(10):
    ttl.forward(10)
    ttl.penup()
    ttl.forward(10)
    ttl.pendown()


screen = Screen()
screen.exitonclick()