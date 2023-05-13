"""正方形内切圆填充红色，并画一个外接圆"""
import turtle
from turtle import *
turtle.fd(250)
turtle.right(90)
turtle.fd(250)
turtle.right(90)
turtle.fd(250)
turtle.right(90)
turtle.fd(250)
turtle.right(90)
turtle.fd(125)
turtle.pencolor("red")
turtle.fillcolor("red")
begin_fill() # 开始填充红色
turtle.circle(-125) # 内接圆
end_fill() # 结束填充
turtle.circle(125) # 外接圆
turtle.hideturtle()
mainloop()