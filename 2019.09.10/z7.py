
import turtle
t=turtle

t.shape('turtle')
k=1 #коэффицент увеличения шага
a=0.35 #начальная длина шага
while 1:
	t.speed(10)	
	t.forward(a*k)
	t.left(360/100)
	k+=0.01
	
