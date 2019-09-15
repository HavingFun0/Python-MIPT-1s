
import turtle as t
t.speed(10)

def dyga(v:int,n:int):
	for i in range(n):
		t.forward(v)
		t.right(180/n)
		t.forward(v)


t.shape('turtle')
a=3 #начальная длина стороны фигуры
n=42 #количество сторон большего многоугольника
k=6 #коэффицент уменьшения радиуса второй дуги по сравнению с первой
t.left(90)
t.penup()
t.goto(-420,0) #удлинение пружинки
t.pendown()
while 1:
	dyga(a,n)
	dyga(a,n//k)
