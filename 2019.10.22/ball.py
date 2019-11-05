import target
import circle
class ball(circle.circle):  # Класс пуля
    def __init__(self, canv):
        super().__init__(canv)

    def move(self, canv):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 4
        fl = 1
        if (self.x + self.r + self.vx >= 800) or (self.x - self.r + self.vx <= 0):
            self.vx *= -0.5
        if (self.y + self.r - self.vy + g / 2 >= 600) or (self.y - self.r - self.vy + g / 2 <= 0):
            self.vy *= -0.8
            if (self.y + self.r - self.vy + g / 2 >= 600):
                fl = 0
        self.x += self.vx
        if fl:
            self.vy -= g
            self.y -= self.vy - g / 2
        else:
            self.vy = 0
            g = 0
        canv.move(self.id, self.vx, -self.vy + g / 2)

    def hittest(self, canv, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели, и удаляет цель. В противном случае возвращает False.
        """
        if (self.x - obj.x) * (self.x - obj.x) + (self.y - obj.y) * (self.y - obj.y) - (self.r + obj.r) * (self.r + obj.r) <= 0:
            obj.hit(canv)
            return True
        else:
            return False
