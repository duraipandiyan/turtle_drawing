import turtle as t
import time
t.begin_fill()
t.bgcolor("black")
t.color("black","green")
t.speed(10)
t.circle(90)
t.color("green")
n=100
for i in range(n):
    n-=10
    if n==-100:
        break
    t.circle(n)
t.forward(20)
t.begin_fill()
t.color("blue")
t.right(90)
t.circle(90)
n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.begin_fill()
t.color("red")
t.forward(80)
t.circle(90)

n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.begin_fill()
t.color("pink")
t.forward(20)
t.circle(90)

n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.begin_fill()
t.color("white")
t.forward(20)

n=100
while 1<=n:
    n-=10
    t.circle(n)
t.mainloop()
