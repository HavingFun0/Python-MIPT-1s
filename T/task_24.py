#!/usr/bin/python3

from pyrob.api import *

def krest():
    move_down()
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_up(3)

@task
def task_2_1():
    move_right(2)
    for i in range(1):
        krest()
       
    move_left()
    move_down()


if __name__ == '__main__':
    run_tasks()
