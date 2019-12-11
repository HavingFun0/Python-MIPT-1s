# coding=utf-8
from random import choice


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
