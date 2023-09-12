from turtle import *

speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(3)
for i in range(100, 0, -5):
    fd(i)
    lt(360/4)
    write(i)
    
hideturtle()
mainloop()
