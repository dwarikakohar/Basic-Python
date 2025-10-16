import turtle as t
import math
import random
t.bgcolor("black")
t.speed(0)
while True:
    r = random.randint(1,50)
    b = random.randint(1,80)
    c = random.randint(1,30)
    d = random.randint(1,10)
#    for i in range(100)
    t.pencolor("orange")
    t.forward(r)
    t.right(d)
    t.circle(b)
    t.forward(math.pi)
    
        