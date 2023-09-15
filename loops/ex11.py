from turtle import *
speed('fastest')

move = 5
while True:

    for i in range(6):
        # fd(100)
        fd(100 + move)
        rt(60)
        pencolor('yellow')
        fillcolor('red')
        begin_fill()
        for i in range(6):
            fd(50)
            rt(60)
        rt(60)
        move += 5
        end_fill()
    pencolor('green')
hideturtle()
mainloop()