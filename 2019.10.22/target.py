import circle
from random import randrange as rnd, choice
class target(circle.circle):  # Класс мишень
    def __init__(self, canv):
        self.canv = canv
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

    def new_target(self, canv):
        """ Инициализация новой цели. """
        super().__init__(canv, rnd(600, 750), rnd(300, 550),  # (canv, x, y, r, vx, vy, Ax, Ay)
                         rnd(20, 50), rnd(5, 15), -rnd(5, 15),
                         rnd(150, 320), rnd(100, 180)
                         )
        self.live = 1
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, canv, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

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


