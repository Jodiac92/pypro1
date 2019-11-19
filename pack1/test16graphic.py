# 그래픽 지원 모듈 중 turtle
import turtle
# a = turtle.Pen()
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# a.forward(100)

from turtle import *
p = turtle.Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()