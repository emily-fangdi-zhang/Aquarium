import random
import utilities
import tkinter as tk
import time

def make_landscape_object(canvas, position, size=100, color="#315717", secondary_color="#B99095", rocks_int=100):
    # your code to create your creature goes here:
    # replace the code below...
    print('make_landscape_object...')
    print('size:', size, 'center:', position)

    for i in range(size):
        x = random.randint(20, 1500)
        y = random.randint(30, 700)
        utilities.make_bubble(canvas, (x, y), 10)

    for i in range(size):
        x = random.randint(20, 1500)
        y = random.randint(30, 700)
        utilities.make_bubble(canvas, (x, y), 5, outline="blue")

    for i in range(0, (2 * size)):
        x = random.randint(20, 1500)
        y = random.randint(650, 700)
        utilities.make_cloud(canvas, (x, y))

    # seaweed 1
    utilities.make_rectangle(canvas, (50, 300), 35, 500, fill_color=color)
    
    utilities.make_rectangle(canvas, (85, 300), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (15, 350), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (85, 400), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (15, 450), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (85, 500), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (15, 550), 35, 35, fill_color=color)

    # seaweed 2
    utilities.make_rectangle(canvas, (850, 500), 35, 500, fill_color=color)
    
    utilities.make_rectangle(canvas, (885, 500), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (815, 550), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (885, 600), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (815, 650), 35, 35, fill_color=color)

    # seaweed 3
    utilities.make_rectangle(canvas, (1000, 300), 35, 500, fill_color=color)
    
    utilities.make_rectangle(canvas, (1035, 300), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (965, 350), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (1035, 400), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (965, 450), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (1035, 500), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (965, 550), 35, 35, fill_color=color)

    # seaweed 4
    utilities.make_rectangle(canvas, (1200, 500), 35, 500, fill_color=color)
    utilities.make_rectangle(canvas, (1235, 550), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (1165, 650), 35, 35, fill_color=color)

    # seaweed 5
    utilities.make_rectangle(canvas, (200, 500), 35, 500, fill_color=color)
    utilities.make_rectangle(canvas, (235, 550), 35, 35, fill_color=color)
    utilities.make_rectangle(canvas, (165, 650), 35, 35, fill_color=color)

    # rocks
    for i in range(rocks_int):
        x = random.randint(50, 1300)
        y = random.randint(600, 670)
        utilities.make_rectangle(canvas, (x, y), 15, 20, fill_color=secondary_color, tag="rocks")

    
