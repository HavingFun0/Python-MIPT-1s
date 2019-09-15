

import turtle
turtle.shape('turtle')

t=turtle
n=int(input("Введите n:"))
t.shape('turtle')
a=100 #длина лапы
for i in range(n):
	t.forward(100)
	t.stamp()
	t.backward(100)
	t.left(360 / n)

