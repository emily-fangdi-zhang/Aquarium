import os
import random
import math

_cache = []
def _get_coordinates(canvas, id):
    return canvas.coords(id)

def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def _update_position_by_id(canvas, id, x=2, y=0):
    coords = _get_coordinates(canvas, id)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y
    # set the coordinates:
    _set_coordinates(canvas, id, coords)

def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')

def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')

def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords

def make_circle(canvas, center, radius, fill_color='#FF4136', tag=None, stroke_width=2, outline=None):
    make_oval(
        canvas, center, radius, radius, fill_color=fill_color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, fill_color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=fill_color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def make_poly_circle(canvas, center, radius, fill_color='#FF4136', tag=None, stroke_width=1, outline=None):
    make_poly_oval(
        canvas,
        center,
        radius,
        radius,
        fill_color=fill_color,
        tag=tag,
        stroke_width=stroke_width,
        outline=outline)

def make_poly_oval(canvas, center, radius_x, radius_y, fill_color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    x0, y0, x1, y1 = (x - radius_x, y - radius_y, x + radius_x, y + radius_y)

    steps = 100
    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    # center
    xc = x0 + a
    yc = y0 + b

    point_list = []

    # create the oval as a list of points
    for i in range(steps):
        # Calculate the angle for this step
        theta = (math.pi * 2) * (float(i) / steps)

        x = a * math.cos(theta)
        y = b * math.sin(theta)

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return canvas.create_polygon(
        point_list,
        fill=fill_color,
        width=stroke_width,
        tags=tag,
        outline=outline,
        smooth=True
    )

def rotate(canvas, tag, degrees=5, origin=None):
    # NOTE: This rotate function only works on POLYGONS
    # DOES NOT WORK ON circles or ovals
    if origin is None:
        # calculate reasonable origin
        top = get_top(canvas, tag)
        bottom = get_bottom(canvas, tag)
        left = get_left(canvas, tag)
        right = get_right(canvas, tag)
        origin = (right - left, bottom - top)

    degrees = math.radians(degrees)
    ox, oy = origin

    shape_ids = canvas.find_withtag(tag)
    for id in shape_ids:
        coords = _get_coordinates(canvas, id)
        # update coordinates:
        for i in range(0, len(coords), 2):
            px, py = coords[i], coords[i+1]
            qx = ox + math.cos(degrees) * (px - ox) - math.sin(degrees) * (py - oy)
            qy = oy + math.sin(degrees) * (px - ox) + math.cos(degrees) * (py - oy)
            coords[i] = qx
            coords[i+1] = qy
        # set the coordinates:
        _set_coordinates(canvas, id, coords)

def make_square(canvas, top_left, width, fill_color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + width)],
        fill=fill_color,
        width=0,
        tags=tag
    )

def make_rectangle(canvas, top_left, width, height, fill_color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)],
        fill=fill_color,
        width=0,
        tags=tag
    )

def make_line(canvas, coordinates, curvy=False, width=2, tag=None):
    canvas.create_line(
        coordinates,
        width=width,
        smooth=curvy,
        tag=tag)

def get_left(canvas, tag):
    '''
    returns the left boundary of the shape group
    '''
    return min(*_get_x_coordinates(canvas, tag))

def get_right(canvas, tag):
    '''
    returns the right boundary of the shape group
    '''
    return max(*_get_x_coordinates(canvas, tag))

def get_top(canvas, tag):
    '''
    returns the top boundary of the shape group
    '''
    return min(*_get_y_coordinates(canvas, tag))

def get_bottom(canvas, tag):
    '''
    returns the bottom boundary of the shape group
    '''
    return max(*_get_y_coordinates(canvas, tag))

def get_width(canvas, tag):
    '''
    returns the width of the shape group
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)

def get_center(canvas, tag):
    return get_width(canvas, tag) / 2 + get_left(canvas, tag)


def get_height(canvas, tag):
    '''
    returns the height of the shape group
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)

def make_cloud(canvas, center, my_tag=""):
    for i in range(random.randint(0,10)):
        x_offset = random.randint(-40,40)
        y_offset = random.randint(0,20)
        make_circle(canvas, (center[0] + x_offset, center[1] + y_offset), random.randint(10,50), fill_color="#7A5230", tag=my_tag, outline="#7A5230")

def make_car(canvas, top_left=(0, 0), fill_color="#3D9970", my_tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    x, y = top_left
    make_rectangle(canvas, (x + 50, y), 100, 40, fill_color=fill_color, tag=my_tag)
    make_rectangle(canvas, (x, y + 30), 200, 45, fill_color=fill_color, tag=my_tag)
    make_circle(canvas, (x + 50, y + 80), 20, fill_color='black', tag=my_tag)
    make_circle(canvas, (x + 150, y + 80), 20, fill_color='black', tag=my_tag)

def make_star(canvas, center, diameter, my_tag=""):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        fill_color='white',
        tag=my_tag
    )

def make_bubble(canvas, center, diameter, outline='white', stroke_width=1, my_tag="", **kwargs):
    '''
    demo function that show you how to draw a bubble, given the convenience
    functions that are available in this module
    '''
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=stroke_width,
        outline=outline,
        fill_color=None,
        tag=my_tag,
        **kwargs
    )

def make_image(
        canvas, image_path, position=(200, 200), rotation=None,
        scale=None, anchor='nw', **kwargs):
    # import PIL libraries
    from PIL import Image, ImageTk

    # 1. create PIL image and apply any image transformations:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(dir_path, image_path)
    pil_image = Image.open(image_path)
    print(scale)
    if scale:
        size = (
            round(pil_image.size[0] * scale),
            round(pil_image.size[1] * scale)
        )
        pil_image = pil_image.resize(size)
    if rotation:
        pil_image = pil_image.rotate(rotation)  # note: returns a copy

    # 2. convert to tkinter-compatible image format:
    tkinter_image = ImageTk.PhotoImage(pil_image)
    _cache.append(tkinter_image)  # workaround for known tkinter bug: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm

    # 3. draw image on canvas:
    canvas.create_image(*position, image=tkinter_image, anchor=anchor, **kwargs)

def get_tag_from_x_y_coordinate(canvas, x, y):
    try:
        shape_id = canvas.find_closest(x, y) # get the top shape
        if shape_id:
            tags = canvas.gettags(shape_id)
            if len(tags) > 0:
                # print(tags)
                return tags[0]
        return None
    except:
        print('error: none found')
        return None

def update_position_by_tag(canvas, tag, x=2, y=0):
    ids = canvas.find_withtag(tag)
    for id in ids:
        _update_position_by_id(canvas, id, x, y)

def update_fill_by_tag(canvas, tag, color):
    ids = canvas.find_withtag(tag)
    for id in ids:
        canvas.itemconfig(id, fill=color)

def delete_by_tag(canvas, tag):
    ids = canvas.find_withtag(tag)
    for id in ids:
        canvas.delete(id)


def flip(canvas, tag):
    center = get_center(canvas, tag)
    width = get_width(canvas, tag)
    shape_ids = canvas.find_withtag(tag)
    for shape_id in shape_ids:
        flipped_coordinates = []
        shape_coords = _get_coordinates(canvas, shape_id)
        counter = 0
        for num in shape_coords:
            if counter % 2 == 0:
                if num < center:
                    flipped_coordinates.append(num + 2 * (center - num))
                elif num > center:
                    flipped_coordinates.append(num - 2 * (num - center))
                else:
                    flipped_coordinates.append(num)
            else:
                flipped_coordinates.append(num)
            counter += 1
        _set_coordinates(canvas, shape_id, flipped_coordinates)


def make_grid(c, w, h):
    interval = 100

    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, interval):
            c.create_line(0, i, w, i, tag='grid_line')

            # Creates axis labels
            offset = 2
            for y in range(0, h, interval):
                for x in range(0, w, interval):
                    c.create_oval(
                    x - offset,
                    y - offset,
                    x + offset,
                    y + offset,
                    fill='black'
                    )
                    c.create_text(
                    x + offset,
                    y + offset,
                    text="({0}, {1})".format(x, y),
                    anchor="nw",
                    font=("Purisa", 8)
                    )
