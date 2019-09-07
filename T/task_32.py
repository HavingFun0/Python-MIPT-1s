#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    v=0
    while wall_is_beneath():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    v=v+1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        else:
            fill_cell()
        mov('ax',v)
        move_right()

if __name__ == '__main__':
    run_tasks()
