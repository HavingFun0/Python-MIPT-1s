import polygons
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas["width"] = 1200
canvas["height"] = 600

for i in polygons.frame:
    canvas.create_polygon(i, fill="#dac783",
                          width=1.0, outline="#dfd28e"
                          )

for i in polygons.left_arm:
    canvas.create_polygon(i, fill="#e3a983",
                          width=1.0, outline="#cd885f",
                          tags='leftarm'
                          )
for i in polygons.right_arm:
    canvas.create_polygon(i, fill="#e3a983",
                          width=1.0, outline="#cd885f",
                          tags='rightarm'
                          )


def hand_move(delta, fl, arm, dx, dy):
    """Движение правой руки """
    if delta < 15 and fl:
        delta += 1
        canvas.move(arm, dx, dy)
    elif delta > 0 and (not fl):
        delta += -1
        canvas.move(arm, -dx, -dy)
    if delta == 15:
        fl = False
    elif delta == 0:
        fl = True

    canvas.after(15, lambda: hand_move(delta, fl, arm, dx, dy))

delta = 0
fl = True
canvas.grid(sticky="nwes")
canvas.move('leftarm', -15, 0)
canvas.move('rightarm', 5, 0)
hand_move(delta, fl, 'rightarm', 0, 1)  # Вызов функции движение правой руки
hand_move(delta, fl, 'leftarm', 1, 0)  # Вызов функции движение левой руки
root.mainloop()
