from turtle import Turtle, Screen

ttl = Turtle()
ttl.shape('turtle')
ttl.color('teal')

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ttl.left(angle)
        ttl.forward(100)


for shape_side in range(3, 13):
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()