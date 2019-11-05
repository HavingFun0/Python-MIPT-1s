# coding=utf-8
import math
import time
import tkinter as tk
from random import randrange as rnd, choice

tk.root = tk.Tk()
screen_width = 800
screen_height = 600
text_position_x = 400
text_position_y = 10
points = 0  # Количество очков

tk.root.geometry(str(screen_width) + 'x' + str(screen_height))

colors = ['red', 'orange', 'yellow',
          'green', 'blue']

tk.canv = tk.Canvas(tk.root, width=800, height=600, bg='white')
tk.canv.pack(fill=tk.BOTH, expand=1)
text = tk.canv.create_text(text_position_x,
                           text_position_y, justify=tk.CENTER,
                           text="Количество очков : " + str(points),
                           font="Verdana 14"
                           )


# Описание класса шарик
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
                                       fill=choice(colors), width=0
                                       )
        self.collision_with = []
        self.interior_ball = second_target(x, y, r, Vx, Vy)

    # Объект шарик на холсте
    # Метод для движения шарика
    def move_ball(self, balls):
        global screen_width, screen_height
        tk.canv.move(self.obj, self.Vx, self.Vy)
        tk.canv.move(self.interior_ball.obj, self.Vx, self.Vy)
        self.interior_ball.x += self.Vx
        self.interior_ball.y += self.Vy
        self.x += self.Vx
        self.y += self.Vy
        if (self.x + self.Vx + self.r >= screen_width) or (self.x + self.Vx - self.r <= 0):
            self.Vx = -1 * self.Vx
        elif (self.y + self.Vy + self.r >= screen_height) or (self.y + self.Vy - self.r <= 0):
            self.Vy = -1 * self.Vy
        for b in balls:
            if (self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y) - (self.r + b.r) * (
                    self.r + b.r) < 0 and b.count != self.count:
                for q in self.collision_with:
                    if q != b.count:
                        self.reflect(b)
                if len(self.collision_with) == 0:
                    self.reflect(b)

    # Мeтод удаления и замены двух шариков
    def delete_ball(self):
        tk.canv.delete(self.obj)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(40, 60)
        self.Vx = rnd(-15, 15)
        self.Vy = rnd(-15, 15)
        self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
                                       self.x + self.r, self.y + self.r,
                                       fill=choice(colors), width=0
                                       )
        tk.canv.delete(self.interior_ball.obj)
        self.interior_ball = second_target(self.x, self.y, self.r, self.Vx, self.Vy)

    # Отражение шариков друг от друга
    def reflect(self, ref_ball):
        ball2_vx = ref_ball.Vx
        ball2_vy = ref_ball.Vy
        ball1_vx = self.Vx
        ball1_vy = self.Vy
        if ref_ball.x - self.x != 0:
            a = math.atan(math.atan((ref_ball.y - self.y) / (ref_ball.x - self.x)))  # Угол разлета
        else:
            a = math.pi / 2
        sin_a = math.sin(a)
        cos_a = math.cos(a)
        self.Vx = ball2_vx * cos_a * cos_a + sin_a * cos_a * ball2_vy - sin_a * cos_a * ball1_vy + sin_a * sin_a * ball1_vx
        self.Vy = ball2_vx * cos_a * sin_a + sin_a * sin_a * ball2_vy + cos_a * cos_a * ball1_vy - sin_a * cos_a * ball1_vx

        ref_ball.Vx = ball1_vx * cos_a * cos_a + sin_a * cos_a * ball1_vy - sin_a * cos_a * ball2_vy + sin_a * sin_a * ball2_vx
        ref_ball.Vy = ball1_vx * cos_a * sin_a + sin_a * sin_a * ball1_vy + cos_a * cos_a * ball2_vy - sin_a * cos_a * ball2_vx
        ref_ball.collision_with.append(self.count)


class second_target():
    def __init__(self, x_center, y_center, r, Vx_big, Vy_big):
        self.x = rnd(x_center - r // 2, x_center + r // 2)
        self.y = rnd(y_center - r // 2, y_center + r // 2)
        self.r = rnd(10, 17)
        self.Vx = Vx_big + rnd(3, 7)
        self.Vy = Vy_big + rnd(3, 7)
        self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
                                       self.x + self.r, self.y + self.r,
                                       fill='Black', width=0
                                       )

    #   self.obj = tk.canv.create_oval(self.x - self.r, self.y - self.r,
    #                                  self.x + self.r, self.y + self.r,
    #                                  fill = Black, width=0
    #                                  )


# Обработка события нажатия левой кнопки мыши
def click(event, all_balls):
    # Зачисление очков за шарик
    global text, points
    for i in range(len(all_balls)):
        if all_balls[i].x != event.x and all_balls[i].y != event.y:
            r_to_the_center = math.sqrt(
                (event.x - all_balls[i].x) * (event.x - all_balls[i].x) + (event.y - all_balls[i].y) * (
                        event.y - all_balls[i].y))
        else:
            r_to_the_center = 0
        if r_to_the_center <= all_balls[i].r:
            points += 1
            if r_to_the_center <= all_balls[i].interior_ball.r:
                points += 2
            all_balls[i].delete_ball()
            text_x = 400
            text_y = 10
            tk.canv.delete(text)
            text = tk.canv.create_text(text_x,
                                       text_y, justify=tk.CENTER,
                                       text="Количество очков : " + str(points),
                                       font="Verdana 14"
                                       )


def safe_result():
    """Сохранение результатов"""
    global points
    lines = ''
    with open('results.txt', 'r') as results:
        opend_file = results.readlines()
        j = 0
        while len(opend_file) > j:
            if opend_file[j] == '\n':
                opend_file.remove('\n')
                j -= 1
            j += 1
        j = 0
        if len(opend_file) == 0:
            opend_file.append(str(points))
        else:
            while len(opend_file) > j and int(opend_file[j][0]) >= points:
                j += 1
            opend_file.insert(j, str(points) + '\n')
        for line in opend_file:
            lines += line
    with open('results.txt', 'w') as results:
        results.write(lines)
    tk.root.destroy()


print('Click right mouse button to end the game and safe results')
# Создание списка шариков
n = 4  # int(input())#Количество шариков на экране
list_of_balls = []
for i in range(n):
    list_of_balls.append(ball(rnd(100, 700), rnd(100, 500),  # x, y, r, Vx, Vy
                              rnd(40, 60), rnd(-20, 20),
                              rnd(-20, 20)
                              )
                         )


def main():
    j = 0
    # Движение всех объектов
    while j < len(list_of_balls):
        list_of_balls[j].move_ball(list_of_balls)
        j += 1
    j = 0
    while j < len(list_of_balls):
        list_of_balls[j].collision_with.clear()
        j += 1
    tk.root.after(70, main)


tk.canv.bind('<Button-3>', safe_result)
tk.canv.bind('<Button-1>', lambda event: click(event, list_of_balls))
main()
tk.mainloop()
