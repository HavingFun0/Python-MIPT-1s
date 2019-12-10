import image
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas["width"] = 1200
canvas["height"] = 600

for i in image.frame:
    canvas.create_polygon(i, fill="#dac783",
                          width=1.0, outline="#dfd28e"
                          )

for i in image.left_arm:
    canvas.create_polygon(i, fill="#e3a983",
                          width=1.0, outline="#cd885f",
                          tags='leftarm'
                          )
for i in image.right_arm:
    canvas.create_polygon(i, fill="#e3a983",
                          width=1.0, outline="#cd885f",
                          tags='rightarm'
                          )


def right_hand_move(delta, up):
    """Движение правой руки """
    if delta < 15 and up:
        delta += 1
        canvas.move('rightarm', 0, 1)
    elif delta > 0 and (not up):
        delta += -1
        canvas.move('rightarm', 0, -1)
    if delta == 15:
        up = False
    elif delta == 0:
        up = True

    canvas.after(15, lambda: right_hand_move(delta, up))


def left_hand_move(delta, right):
    """Движение левой руки
    """
    if delta < 15 and right:
        delta += 1
        canvas.move('leftarm', 1, 0)
    elif delta > 0 and (not right):
        delta += -1
        canvas.move('leftarm', -1, 0)
    if delta == 15:
        right = False
    elif delta == 0:
        right = True

    canvas.after(15, lambda: left_hand_move(delta, right))


delta = 0
up = True
right = True
canvas.grid(sticky="nwes")
canvas.move('leftarm', -15, 0)
canvas.move('rightarm', 5, 0)
right_hand_move(delta, up)  # Вызов функции движение правой руки
left_hand_move(delta, right)  # Вызов функции движение левой руки
root.mainloop()
