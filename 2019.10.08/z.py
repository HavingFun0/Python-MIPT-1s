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
	math.pi / 3 / 9 #Убери это, либо используй 
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
    count = 0
    def __init__(self, x, y, r, Vx, Vy):
        ball.count += 1
        self.count = ball.count
        self.x = x 
        self.y = y
        self.r = r
        self.Vx = Vx
        self.Vy = Vy
        self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
                self.x + self.r, self.y + self.r,
				    fill = choice(colors), width = 0
    )    
#Объект шарик на холсте
    # Метод для движения шарика
    def move_ball(self, balls):
        global screen_width, screen_height
        tk.canv.move(self.obj, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy
        if (self.x + self.Vx + self.r >= screen_width) or (self.x + self.Vx - self.r <= 0):
            self.Vx = -1 * self.Vx 
        elif (self.y + self.Vy + self.r >= screen_height) or (self.y + self.Vy - self.r <= 0): 
            self.Vy = -1 * self.Vy
        for b in balls: 
            if (self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y) - (self.r + b.r) * (self.r + b.r) <=0 and b.count != self.count:
                self.reflect(b)

#Мeтод удаления и замены шарика 
    def delete_ball(self):
        tk.canv.delete(self.obj)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.Vx = rnd(-40, 40)
        self.Vy = rnd(-40, 40)
        self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
    	   			    self.x + self.r, self.y + self.r,
				    fill = choice(colors), width = 0
        )

#Отражение шариков друг от друга
    def reflect(self, ball): #TODO! Шарики не должный слипаться! Модель соударений в теории упругости? Ещё варианты? 
        flx = ball.Vx
        fly = ball.Vy
        ball.Vx = self.Vx
        ball.Vy = self.Vy
        self.Vx = flx
        self.Vy = fly


"""
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
"""

#Обработка события нажатия левой кнопки мыши
def click(event):
    global list_of_balls, b, k, text
#Зачисление очков за шарик 
    for i in range(len(list_of_balls)):
        if list_of_balls[i].x != event.x and list_of_balls[i].y != event.y:
            r_to_the_center = math.sqrt((event.x - list_of_balls[i].x) * (event.x - list_of_balls[i].x) + (event.y - list_of_balls[i].y) * (event.y - list_of_balls[i].y))
        else:
            r_to_the_center = 0
        if r_to_the_center <= list_of_balls[i].r:
            k += 1
            list_of_balls[i].delete_ball()
            text_position_x = 400
            text_position_y = 10 
            tk.canv.delete(text)
            text = tk.canv.create_text(text_position_x,	
     	    		text_position_y, justify = tk.CENTER,  
 	    		text = "Количество очков : " + str(k),
 	                font = "Verdana 14"	
            )






#Создание списка шариков
n = 11#int(input())#Количество шариков на экране
list_of_balls = [] 
for i in range(n):
    list_of_balls.append(ball(rnd(100, 700), rnd(100,500),  #x, y, r, Vx, Vy 
                  rnd(30,50), rnd(-30, 30), 
                  rnd(-30,30)
                 )    
    )
"""
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
"""


	



def main():
    global list_of_balls, b
    i = 0
#Движение всех объектов
    while i < len(list_of_balls):
        list_of_balls[i].move_ball(list_of_balls)      
        i += 1
    tk.root.after(70, main)

    
   
        


tk.canv.bind('<Button-1>', click)
main()
tk.mainloop()

