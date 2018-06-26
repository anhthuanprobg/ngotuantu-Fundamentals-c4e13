from turtle import *
h=3
for i in ("blue","red","blue","red"):
    for k in range(h):
        color(i)
        forward(100)
        left(360/h)
    h=h+1    

mainloop()
