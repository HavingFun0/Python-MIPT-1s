#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    k=1
    b=0
    while k:
        move_right()
        if cell_is_filled():
            b=b+1
        if b==5:
            k=0


if __name__ == '__main__':
    run_tasks()
