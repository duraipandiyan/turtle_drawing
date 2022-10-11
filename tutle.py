import turtle as t
import time
t.begin_fill()
t.color("black","green")
t.speed(10)
t.circle(90)
n=100
for i in range(n):
    n-=10
    if n==-100:
        break
    t.circle(n)
t.forward(20)
t.right(90)
t.circle(90)
n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.forward(80)
t.circle(90)
n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.forward(20)
t.circle(90)
n=100
while 1<=n:
    n-=10
    t.circle(n)
t.right(90)
t.forward(20)
n=100
while 1<=n:
    n-=10
    t.circle(n)



t.end_fill()
t.mainloop()
