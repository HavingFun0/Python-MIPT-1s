import time
import turtle as t
t.speed(10)

def kryg(v:int,n:int,napravlenie:bool):
	if napravlenie:
		for i in range(n):
			t.forward(v)
			t.left(360/n)
			t.forward(v)
	else:
		for i in range(n):
			t.forward(v)
			t.right(360/n)
			t.forward(v)
       

t.shape('turtle')
a=4 #начальная длина стороны фигуры
n=60 #количество сторон многоугольника

for i in range(3):
	kryg(a,n,1)
	kryg(a,n,0)
	t.right(60)

time.sleep(4)
