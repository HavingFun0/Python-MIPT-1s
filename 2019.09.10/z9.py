import time
import math
import turtle as t
t.speed(6)

def mnogoygolnik(i:int,v:int):
	t.left(90+180/i)
	for j in range(i):
		t.forward(v)
		t.left(360/i)
	t.right(90+180/(i))

t.shape('turtle')
k=3 #количество сторон многоугольника
a=38 #начальная длина сторонa фигуры


for i in range(10):
	R=a/(2*math.sin(math.radians(180/k))) #радиус описанной окружности
	t.penup()
	t.goto(R,0)
	t.pendown()
	mnogoygolnik(k,a)
	t.penup()
	k+=1
	t.pendown()
	a=R*2*math.tan(math.radians(360/(2*(k-1))))
time.sleep(4)
