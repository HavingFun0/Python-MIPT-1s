#!/usr/bin/python3

from pyrob.api import *
        

@task(delay=0.001)
def task_8_30():
    k=1
    while k:
        while wall_is_beneath() and not wall_is_on_the_left():
            move_left()
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
        else:
            while wall_is_beneath() and not wall_is_on_the_right():
                move_right()
            if wall_is_on_the_right():
                k=0
            if k:
                while not wall_is_beneath():
                    move_down()               
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
