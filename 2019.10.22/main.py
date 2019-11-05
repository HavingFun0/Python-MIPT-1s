import ball
import circle
import gun
import target
import time
import tkinter as tk

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
canv.create_line(0, 600, 800, 600, width=9)

target1 = target.target(canv)
target2 = target.target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun.gun(canv)


def new_game(event=''):
    """Сама игра"""
    global target1, screen1, target2

    target1.new_target(canv)
    target2.new_target(canv)
    bullet = []
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', lambda event: g1.fire2_end(event, balls, bullet))
    canv.bind('<Motion>', lambda event: g1.targetting(canv, event))

    z = 0.03
    target1.live = 1
    target2.live = 1
    while target1.live or balls or target2.live:
        for ball in balls:
            ball.move(canv)
            ball.live -= 1
            if ball.live <= 0:
                canv.delete(ball.id)
                balls.remove(ball)
            if ball.hittest(canv, target1) and target1.live:
                target1.live = 0
            if ball.hittest(canv, target2) and target2.live:
                target2.live = 0
            if not target2.live and not target1.live:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(len(bullet)) + ' выстрелов')
        target1.move(canv)
        target2.move(canv)
        canv.update()
        time.sleep(0.03)
        g1.targetting(canv)
        g1.power_up(canv)
    canv.itemconfig(screen1, text='')
    canv.delete(gun.gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
