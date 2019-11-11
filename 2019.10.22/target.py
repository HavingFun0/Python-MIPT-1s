# coding=utf-8
from random import randrange as rnd

import circle


class target(circle.circle):  # Класс мишень
    points = 0
    id_points = 0

    def __init__(self, canv):
        """ Инициализация новой цели. """
        super().__init__(canv, rnd(600, 750), rnd(300, 550),  # (canv, x, y, r, vx, vy, Ax, Ay)
                         rnd(20, 50), rnd(5, 15), -rnd(5, 15),
                         rnd(150, 320), rnd(100, 180)
                         )
        self.live = 1

    def hit(self, canv, text_scope, point=1):
        """Попадание шарика в цель."""
        target.points += point
        self.y = -100
        canv.itemconfig(text_scope, text=target.points)

    def move(self, canv):
        """Движение мишени"""
        if (self.x + self.vx >= self.x0 + self.Ax) or (self.x + self.vx + self.r >= 800):
            self.vx *= -0.95
        elif (self.x + self.vx <= self.x0 - self.Ax) or (self.x + self.vx - self.r <= 0):
            self.vx *= -0.95
        self.x += self.vx
        if (self.y + self.vy <= self.y0 - self.Ay) or (self.y + self.vy - self.r <= 0):
            self.vy *= -0.95
        elif (self.y + self.vy >= self.y0 + self.Ay) or (self.y + self.vy + self.r >= 600):
            self.vy *= -0.95
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)
