import time
import math
import turtle as t
t.speed(10)

def dyga(v:int,n:int):
	for i in range(n):
		t.forward(v)
		t.left(180/n)
		t.forward(v)
def kryg(v:int,n:int):
	for i in range(n):
		t.forward(v)
		t.left(360/n)
		t.forward(v)


t.shape('classic')
a=3 #длина стороны
n=40 #количество сторон
kface=8 #коэффицент увеличения для лица
y0=-300 #начальная позиция рисования
xg=4*a*kface #координата по x нижней точки глаза
yg=4*a*kface #координата по н нижней точки глаза
lnose=a*n/math.pi #половина длины носа
width=30 #толщина носа и губ
klips=kface/2 #коэффицент увеличения для губ
xl=-a*n*kface/(math.pi*2)              #координата x для левого кончика губы
yl=-a*n*kface/(math.pi*5)              #координата н для левого кончика губы

t.penup()
t.goto(0,y0) 
t.pendown()
t.color('yellow')   #рисование головы смайлика
t.begin_fill()
kryg(a*kface,n)
t.end_fill()

t.color('blue')
t.penup() 
t.goto(xg,yg)
t.pendown()         #рисование правого глаза 
t.begin_fill()
kryg(a,n)
t.end_fill()

t.penup()
t.goto(-xg,yg)
t.pendown()        #рисование левого глаза
t.begin_fill()
kryg(a,n)
t.end_fill()

t.width(width)
t.color('black')
t.penup()
t.goto(0,lnose)           #рисование носа
t.pendown()
t.goto(0,-lnose)

t.color('red')
t.penup()
t.goto(xl,yl)                  #рисование губ
t.pendown()
t.right(90)
dyga(a*klips,n//2)

time.sleep(4)
