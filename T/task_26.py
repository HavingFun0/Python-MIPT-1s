#!/usr/bin/python3

from pyrob.api import *

def krest():
   
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
    move_up(2)



@task(delay=0.001)
def task_2_4():
    move_right()
    for j in range(2):   
        
        krest()
        for i in range(9):
            move_right(4)
            krest()
        move_down(4)
        krest()
        for i in range(9):
            move_left(4)
            krest()
        move_down(4) 
    krest()
    for i in range(9):
        move_right(4)
        krest()
    move_left(37)


    


if __name__ == '__main__':
    run_tasks()
