from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
canv.create_line(0,600,800,600,width=9) 

class circle():
    def __init__(self, canv, x=40, y=450, r=10, vx=0, vy=0, Ax=0, Ay=0):
        """ Конструктор класса круг
  
        Args:
        x0 - начальное положение мячика по горизонтали
        x = x0
        y0 - начальное положение мячика по вертикали
        y = y0
        r - радиус круга
        vx - скорость по горизонтали
        vy - скорость по вертикали 
        Ax - максимальное отклонение от начального положения по горизонтали
        Ay - максимальное отклонение от начального положения по вертикали
        id - объект на холсте
        live - жизни объекта
        """
        self.canv = canv
        self.x = x
        self.x0 = x
        self.y = y
        self.y0 = y
        self.r = r
        self.r0 = r
        self.Ax = Ax
        self.Ay = Ay
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 70

class ball(circle):         #Класс пуля
    def __init__(self, canv):
        super().__init__(canv)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """ 
        g = 4 
        fl = 1
        if (self.x + self.r + self.vx >= 800) or (self.x - self.r + self.vx<= 0):
            self.vx *= -0.5
        if (self.y + self.r - self.vy + g/2>= 600) or (self.y - self.r - self.vy + g/2 <= 0):
            self.vy *= -0.8       
            if (self.y + self.r - self.vy + g/2 >= 600):
                fl = 0
        self.x += self.vx
        if fl:
            self.vy -= g
            self.y -= self.vy - g /2
        else:
            self.vy = 0
            g = 0
        canv.move(self.id, self.vx, -self.vy + g/2)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели, и удаляет цель. В противном случае возвращает False.
        """
        if  (self.x - obj.x) * (self.x - obj.x) +  (self.y - obj.y) * (self.y - obj.y) - (self.r + obj.r) * (self.r + obj.r) <= 0:
            obj.hit()
            return True
        else:
            return False


class gun():    #Класс пушка
    def __init__(self, canv):
        """Инициализания класса пушка
 
        Arg:
        f2_power - сила выстрела
        аn - начальный угол
        f2_on - метка отвечающая на вопрос: а работает ли пушка?
        canv - холст для рисования
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
        self.canv = canv

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, balls, bullet):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        bullet += 1
        new_ball = ball(self.canv)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
        return balls, bullet

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x - 20) != 0:
                self.an = math.atan((event.y-450) / (event.x-20))
            else:
                self.an = math.pi / 2
        if self.f2_on:
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """Увеличение силы выстрела
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target(circle):    #Класс мишень
    def __init__(self, canv):
        self.canv = canv
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')

    def new_target(self, canv):
        """ Инициализация новой цели. """
        super().__init__(canv, rnd(600, 750), rnd(300,550),#(canv, x, y, r, vx, vy, Ax, Ay)
                         rnd(20,50), rnd(5, 15), -rnd(5,15),
                         rnd(150, 320), rnd(100, 180)
        ) 
        self.live = 1
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill = self.color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)
  
    def move(self):
         """Движение мишени"""   
         if (self.x + self.vx >= self.x0 + self.Ax) or (self.x + self.vx + self.r >= 800):
             self.vx *= -0.95
         elif (self.x + self.vx <= self.x0 - self.Ax) or (self.x + self.vx - self.r <= 0):
             self.vx *= -0.95
         self.x += self.vx
         if (self.y + self.vy <= self.y0 - self.Ay) or (self.y + self.vy - self.r<= 0):
             self.vy *= -0.95
         elif (self.y + self.vy >= self.y0 + self.Ay) or (self.y + self.vy + self.r >= 600):
             self.vy *= -0.95
         self.y += self.vy
         canv.move(self.id, self.vx, self.vy)

t1 = target(canv)
t2 = target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun(canv)
bullet = 0
balls = []


def new_game(event=''):
    """Сама игра"""
    global gun, t1, screen1, balls, bullet, t2
    
    t1.new_target(canv)
    t2.new_target(canv)
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', lambda event: g1.fire2_end(event, balls, bullet))
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or balls or t2.live:
        for b in balls:
            b.move()
            b.live -= 1
            if b.live <= 0:
                canv.delete(b.id)
                balls.remove(b)
            if b.hittest(t1) and t1.live:
                t1.live = 0
            if b.hittest(t2) and t2.live:
                t2.live = 0
            if not t2.live and not t1.live:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов') 
        t1.move()
        t2.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
