### EFFECTS IMPLEMENTED ###
#1 I have implemented the animationn where the starfish with the tag "move" will move
#  continuously across the screen until it reaches the left end. After that, it will
#  respawn on the right.
#3 I have inplemented the animation where the user can click to "make" a new starfish
#  anywhere on the screen with the function click_handle.
#5 I have implemented the animation where the user can control the "test" starfish with 
#  w, a, s, and d keys, corresponding to up, left, down and right respectively.
#6 The program I have written will periodically generate a random starfish with different
#  sizes, colors, and centers.
#11 The background color will periodically change from "navy" to "sky blue".

from shutil import move
from tkinter import Canvas, Tk
import utilities
import time
import random

import creature
import landscape

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width,
                height=window_height, background='light blue')
canvas.pack()

MOUSE_CLICK = "<Button-1>"
MOUSE_DRAG = "<B1-Motion>"
KEY_PRESS = "<Key>"
active_tag = "test"

canvas.focus_set()

########################## YOUR CODE BELOW THIS LINE ##############################

# sample code to make a creature:
utilities.make_rectangle(canvas, (0,0), 1440, 900, fill_color='light blue', tag='background')
creature.make_creature(canvas, (400, 400), my_fill='#B5E5CF', my_tag="test")
creature.make_creature(canvas, (150, 400), my_fill='#B5E5CF', my_tag="move")

for i in range(7):
    colors1 = ["#D1E8A1", "#FFD898", "#BEDF7C", "#ACD657", "#7EA829", "#FEE7E6", "#ECFDF1", "#F9EAC2"]
    colors = ["#B99095", "#FCB5AC", "#B5E5CF"]
    c = random.choice(colors)
    x = random.randint(100, 1200)
    y = random.randint(200, 400)
    s = random.randint(50, 100)
    creature.make_creature(canvas, (x, y), size=s, my_fill=c, my_tag="starfish")

landscape.make_landscape_object(canvas, (0, 0))

landscape.make_landscape_object(canvas, (0, 0), size=10, secondary_color="#3D5B59", rocks_int=10)

landscape.make_landscape_object(canvas, (0, 0), size=5, secondary_color="#FCB5AC", rocks_int=10)

landscape.make_landscape_object(canvas, (0, 0), size=50)

landscape.make_landscape_object(canvas, (0, 0), secondary_color="#B5E5CF")

print(utilities.get_center(canvas, "test"))

def click_handle(event):
    colors = ["#B99095", "#FCB5AC", "#B5E5CF"]
    c = random.choice(colors)
    s = random.randint(50, 100)
    creature.make_creature(canvas, (event.x, event.y), size=s, my_fill=c, my_tag="star")

canvas.bind(MOUSE_CLICK, click_handle)

def move_starfish(event):
    distance = 40
    
    if event.keysym == "w":
        utilities.update_position_by_tag(canvas, active_tag, x=0, y=-distance)
    
    if event.keysym == "a":
        utilities.update_position_by_tag(canvas, active_tag, x=-distance, y=0)
    
    if event.keysym == "d":
        utilities.update_position_by_tag(canvas, active_tag, x=distance, y=0)
    
    if event.keysym == "s":
        utilities.update_position_by_tag(canvas, active_tag, x=0, y=distance)

canvas.bind(KEY_PRESS, move_starfish)

counter = 0
while True:
    if utilities.get_left(canvas, "move") >= 1600:
        time.sleep(0.07)
        utilities.update_position_by_tag(canvas, "move", x=-1600, y=0)
        utilities.update_position_by_tag(canvas, "move", x=25, y=0)
        counter += 1
        gui.update()
    
    else:
        time.sleep(.07)
        utilities.update_position_by_tag(canvas, 'move', x=25, y=0)
        counter += 1
        gui.update()

    if counter % 10 == 0:
        utilities.update_fill_by_tag(canvas, 'background', 'light blue')
        c = random.choice(colors)
        x = random.randint(100, 1200)
        y = random.randint(200, 400)
        s = random.randint(50, 100)
        creature.make_creature(canvas, (x, y), size=s, my_fill=c, my_tag="add")
        counter += 2

    elif counter % 25 == 0:
        utilities.update_fill_by_tag(canvas, 'background', 'navy')
        c = random.choice(colors)
        x = random.randint(100, 1200)
        y = random.randint(200, 400)
        s = random.randint(50, 100)
        creature.make_creature(canvas, (x, y), size=s, my_fill=c, my_tag="add")
        counter += 2 


gui.mainloop()

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
