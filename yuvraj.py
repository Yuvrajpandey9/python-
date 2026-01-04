from turtle import*
t=Turtle()
s=Screen()
s.title(' computer ')
s.bgcolor("black")
t.speed(0)
c=("red","yellow","cyan","magenta","violet","blue","green","brown","white")
for i in range(1000):
    t.width(10)
    t.color[i%100]
    t.forward(i)
    t.left(100)

done()
