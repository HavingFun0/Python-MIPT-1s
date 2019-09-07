#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range(6):
        move_right()
        move_down()
        while not wall_is_on_the_right() and not wall_is_beneath():
            fill_cell()
            move_right()
            move_down()
        move_left(2)
        move_up() 
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
            move_up()
        move_down()
    move_down()
    move_right()
    fill_cell()
    move_down()


if __name__ == '__main__':
    run_tasks()
