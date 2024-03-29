# coding=utf-8
import math

import ball


class gun():  # Класс пушка
    def __init__(self, canv):
        """Инициализания класса пушка
 
        Arg:
        force_power - сила выстрела
        аn - начальный угол
        force_on - метка отвечающая на вопрос: а работает ли пушка?
        canv - холст для рисования
        """
        self.force_power = 10
        self.force_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)
        self.canv = canv

    def fire2_start(self, event):
        self.force_on = 1

    def fire2_end(self, event, balls, bullet):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = ball.ball(self.canv)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.force_power * math.cos(self.an)
        new_ball.vy = - self.force_power * math.sin(self.an)
        balls += [new_ball]
        bullet.append(1)
        self.force_on = 0
        self.force_power = 10

    def targetting(self, canv, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x - 20) != 0:
                self.an = math.atan((event.y - 450) / (event.x - 20))
            else:
                self.an = math.pi / 2
        if self.force_on:
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, 20, 450,
                         20 + max(self.force_power, 20) * math.cos(self.an),
                         450 + max(self.force_power, 20) * math.sin(self.an)
                         )

    def power_up(self, canv):
        """Увеличение силы выстрела
        """
        if self.force_on:
            if self.force_power < 100:
                self.force_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
