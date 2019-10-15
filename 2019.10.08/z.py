import tkinter as tk
import math
from random import randrange as rnd, choice
import time
tk.root = tk.Tk()
screen_width = 800
screen_height = 600
text_position_x = 400
text_position_y = 10 
k = 0 # Количество очков
frequency = [  math.pi / 3 / 1, math.pi / 3 / 2, 
	math.pi / 3 / 3, math.pi / 3 / 4, 
	math.pi / 3 / 5, math.pi / 3 / 6, 
	math.pi / 3 / 7, math.pi / 3 / 8, 
	math.pi / 3 / 9
]

tk.root.geometry(str(screen_width)+'x'+str(screen_height))

colors = ['red','orange','yellow',
	'green','blue']

tk.canv = tk.Canvas(tk.root, width=800, height=600, bg='white')
tk.canv.pack(fill=tk.BOTH, expand=1)
text = tk.canv.create_text(text_position_x,	
     	    		text_position_y, justify = tk.CENTER,  
 	    		text = "Количество очков : " + str(k),
 	                font = "Verdana 14"	
)



##Описание класса шарик
class ball:
 
    x = 0 
    y = 0
    r = 0
    Vx = 0 
    Vy = 0 
    obj = 0 #Объект шарик на холсте
    # Метод для движения шарика
    def move_ball(self):
        global screen_width, screen_height
        tk.canv.move(self.obj, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy
        if (self.x + self.Vx + self.r >= screen_width) or (self.x + self.Vx - self.r <= 0):
            self.Vx = -0.9 * self.Vx 
        elif (self.y + self.Vy + self.r >= screen_height) or (self.y + self.Vy - self.r <= 0): 
            self.Vy = -0.9 * self.Vy
#Мeтод удаления и замены шарика 
    def delete_ball(self):
        tk.canv.delete(self.obj)
        self.x = rnd(100, 700)
        self.y = rnd(100, 600)
        self.r = rnd(30, 50)
        self.Vx = rnd(-20, 20)
        self.Vy = rnd(-20, 20)
        self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
    	   			    self.x + self.r, self.y + self.r,
				    fill = choice(colors), width = 0
        )     

#Описание класса квадрат 
class square:
 
    x = 0  
    y = 0
    l = 0 # Длина стороны квадрата
    Ax = 0 #Амплитуда колебаний по x
    Ay = 0 #Амплитуда колебаний по y
    wx = 0 #Частота колебаний по x
    wy = 0 #Частота колебаний по y
    obj = 0 #Объект квадрат на холсте
    # Метод для движения квадрата
    def move_square(self):
        global screen_width, screen_height
        dx = self.Ax * math.sin(self.wx)
        dy = self.Ay * math.cos(self.wy)
        tk.canv.move(self.obj, dx, dy)
        self.x += dx
        self.y += dy
        if (self.x + dx + self.l / 2 >= screen_width) or (self.x + dx - self.l / 2 <= 0):
            self.Ax = -0.9 * self.Ax
        elif (self.y + dy + self.l / 2 >= screen_height) or (self.y + dy - self.l / 2 <= 0): 
            self.Ay = -0.9 * self.Ay
#Мeтод удаления и замены квадрата
    def delete_square(self):
        tk.canv.delete(self.obj)
        self.x = rnd(300, 400)
        self.y = rnd(200, 300)
        self.l = rnd(30, 50)
        self.Ax = rnd(-20, 20)
        self.Ay = rnd(-20, 20)
        self.wx = choice(frequency)
        self.wy = choice(frequency)
        self.obj = tk.canv.create_rectangle(self.x - self.l / 2, self.y - self.l / 2,
    	   			    self.x + self.l / 2, self.y + self.l / 2,
				    fill = choice(colors), width = 0
        )      



#Обработка события нажатия левой кнопки мыши
def click(event):
    global a, b, k, text
#Зачисление очков за шарик 
    for i in range(len(a)):
        if a[i].x != event.x and a[i].y != event.y:
            r_to_the_center = math.sqrt((event.x - a[i].x) * (event.x - a[i].x) + (event.y - a[i].y) * (event.y - a[i].y))
        else:
            r_to_the_center = 0
        if r_to_the_center <= a[i].r:
            k += 1
            a[i].delete_ball()
            text_position_x = 400
            text_position_y = 10 
            tk.canv.delete(text)
            text = tk.canv.create_text(text_position_x,	
     	    		text_position_y, justify = tk.CENTER,  
 	    		text = "Количество очков : " + str(k),
 	                font = "Verdana 14"	
            )

#Зачисление очков за квадрат
    for i in range(len(b)):
        if b[i].x != event.x and b[i].y != event.y:
            r_to_the_center = math.sqrt((event.x - b[i].x) * (event.x - b[i].x) + (event.y - b[i].y) * (event.y - b[i].y))
        else:
            r_to_the_center = 0
        if r_to_the_center <= b[i].l / 2 * math.sqrt(2):
            k += 2
            b[i].delete_square()
            text_position_x = 400
            text_position_y = 10 
            tk.canv.delete(text)
            text = tk.canv.create_text(text_position_x,	
     	    		text_position_y, justify = tk.CENTER,  
 	    		text = "Количество очков : " + str(k),
 	                font = "Verdana 14"	
            )







#Создание списка шариков
n = int(input())#Количество шариков на экране
a = [] 
for i in range(n):
    a.append(ball())    
    a[i].x = rnd(100, 700)
    a[i].y = rnd(100, 600)
    a[i].r = rnd(30, 50)
    a[i].Vx = rnd(-20, 20)
    a[i].Vy = rnd(-20, 20)
    a[i].obj = tk.canv.create_oval(a[i].x - a[i].r, a[i].y - a[i].r,
    				    a[i].x + a[i].r, a[i].y + a[i].r,
				    fill = choice(colors), width = 0
    )    
    
#Создание списка квадратов 
n1 = int(input())#Количество квадратов на экране
b = [] 
for i in range(n1):
    b.append(square()) 
    b[i].Ax = rnd(1, 7)
    b[i].Ay = rnd(1, 7)
    b[i].wx = choice(frequency)
    b[i].wy = math.pi / 3 
    b[i].x = rnd(300, 400)
    b[i].y = rnd(200, 300)
    b[i].l = rnd(30, 50)
    b[i].obj = tk.canv.create_rectangle(b[i].x - b[i].l / 2, b[i].y - b[i].l / 2,
    	   			    b[i].x + b[i].l / 2, b[i].y + b[i].l / 2,
				    fill = choice(colors), width = 0
    )      



	



def main():
    global a,b
    i = 0
#Движение всех объектов
    while i < len(a):
        a[i].move_ball()      
        i += 1
    i = 0
    while i < len(b):
        b[i].move_square()
        i += 1
    tk.root.after(70, main)

    
   
        


tk.canv.bind('<Button-1>', click)
main()
tk.mainloop()

