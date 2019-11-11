import time
import tkinter as tk

import gun
import target

root = tk.Tk()
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
canv.create_line(0, 600, 800, 600, width=9)

x_result_screen = 400
y_result_screen = 300
result_screen = canv.create_text(x_result_screen, y_result_screen, text='', font='28')
x_text_scope = 30
y_text_scope = 30
text_scope = canv.create_text(x_text_scope, y_text_scope, text='0', font='28')
gun1 = gun.gun(canv)


def new_game(event=''):
    """Сама игра"""
    target1 = target.target(canv)
    target2 = target.target(canv)
    bullet = []
    balls = []
    canv.bind('<Button-1>', gun1.fire2_start)
    canv.bind('<ButtonRelease-1>', lambda event: gun1.fire2_end(event, balls, bullet))
    canv.bind('<Motion>', lambda event: gun1.targetting(canv, event))
    target1.live = 1
    target2.live = 1
    while target1.live or balls or target2.live:
        for ball in balls:
            ball.move(canv)
            ball.live -= 1
            if ball.live <= 0:
                canv.delete(ball.id)
                balls.remove(ball)
            if ball.hittest(canv, text_scope, target1) and target1.live:
                target1.live = 0
                canv.delete(target1.id)
            if ball.hittest(canv, text_scope, target2) and target2.live:
                target2.live = 0
                canv.delete(target2.id)
            if not target2.live and not target1.live:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(result_screen, text='Вы уничтожили цели за ' + str(len(bullet)) + ' выстрелов')
        target1.move(canv)
        target2.move(canv)
        canv.update()
        sleeptime = 0.03
        time.sleep(sleeptime)
        gun1.targetting(canv)
        gun1.power_up(canv)
    canv.itemconfig(result_screen, text='')
    canv.delete(gun.gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
