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
a=2.4 #начальная длина стороны фигуры
n=40 #количество сторон многоугольника
t.right(90)
while 1:
        kryg(a,n,1)
        kryg(a,n,0)
        a+=0.6
     


