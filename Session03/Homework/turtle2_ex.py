from turtle import *
import random

speed(-1)
shape("turtle")



for i in range(1,120):
    colors = ["black", "red"]
    color(random.choice(colors))
    forward(i*3)
    left(90)

mainloop()