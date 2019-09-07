#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_7_5():
    k=0
    fl=1
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        k=k+1
        if k==fl:
            fill_cell()
            fl=fl+1
            k=0


if __name__ == '__main__':
    run_tasks()
