from turtle import *

speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(3)
for i in range(1, 500, 20):
    fd(i)
    lt(360/2)
    write(i)
    
hideturtle()
mainloop()