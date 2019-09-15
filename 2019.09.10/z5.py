
import turtle
t=turtle

t.shape('turtle')
k=1 #коэффицент увеличения длины стороны
a=16 #начальная длина сторонa фигуры
angle=90 #сторона фигуры 
start=-8 #начальная позиция по х и у
for i in range(10):
	t.penup()
	t.goto(start*k,start*k)
	t.pendown()
	for j in range(4):
		t.forward(a*k)
		t.left(angle)
	t.penup()
	k+=2



