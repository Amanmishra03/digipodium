from turtle import *

for i in range(6):
    if i == 4: break
    fd(150)
    lt(60)
else:
    penup()
    goto(75,-140)
    pendown()
    write("hexagon", align ='center')   
    
hideturtle()
mainloop()