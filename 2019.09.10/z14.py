import math
import os
import time
import turtle as t
t.speed(10)

t.shape('classic')
 
def star(n,k,l,x,y):
	i=1	
	t.penup()
	t.goto(x+l*math.cos(math.pi*(1/2+2*i)/n),y+l*math.sin(math.pi*(1/2+2*i)/n))	 #в тригонометрических функциях формула Муавра
	t.pendown()
	for j in range(n) :
		if n%2!=0:
			i+=n//2
		else:
			i+=1
		t.goto(l*math.cos(math.pi*(1/2+2*i)/n)+x,y+l*math.sin(math.pi*(1/2+2*i)/n))   

l=170 #длина между вершинами	
n=5 #количество вершин
x=200 #половина расстояния между звездочками 
k=2*math.pi*n-math.pi/2  #разность углов между двумя вершинами решения уравнения z^n=1

t.penup()
t.goto(-x,0)
t.pendown()
star(n,k,l,-x,0)

t.penup()
t.goto(x,0)
t.pendown()
n=11
star(n,k,l,x,0)
time.sleep(3)
