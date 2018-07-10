
from turtle import *

for i in range(4,10):
    for _ in range(i):
        pencolor("red","blue")
        forward(100)
        left(360/i)

mainloop()