#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    k=1
    b=0
    while k and not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            b=b+1
        else:
            b=0
        if b==3:
            k=0



if __name__ == '__main__':
    run_tasks()
