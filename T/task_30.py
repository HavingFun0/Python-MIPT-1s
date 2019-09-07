#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_9_3():
    fl=1
    while not wall_is_on_the_right():
        move_right()
        fl=fl+1
    while not fl==1:
        for i in range(fl-2):
            move_down()
            fill_cell()
        move_down()
        for i in range(fl-2):
            move_left()
            fill_cell()
        move_left()
        for i in range(fl-2):
            move_up()
            fill_cell()
        move_up()
        for i in range(fl-2):
            move_right()
            fill_cell()
        move_down()
        fl=fl-2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
