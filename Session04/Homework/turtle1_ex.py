from turtle import *
shape("turtle")
speed(-1)
color("blue")

for i in range (25):
    for k in range (4):
        forward(100)
        left(90)
    left(360/25)

mainloop() 