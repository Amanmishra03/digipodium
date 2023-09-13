from turtle import Turtle, Screen
tim = Turtle()
my_screen = Screen()
num_sides = my_screen.numinput(title="no. of sides you want", prompt="how many sides you want")
num_sides = int(num_sides)
angle = 360/num_sides
for i in range(num_sides):
    tim.fd(100)
    tim.lt(angle)





my_screen.exitonclick()