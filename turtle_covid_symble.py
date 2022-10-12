import turtle as t
t.speed(10)
t.color("green")
t.bgcolor('black')
t.hideturtle()
b=0
while b<200:
    t.right(b)
    t.fd(b*3)
    b+=1