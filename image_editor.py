import os
import tkinter as tk

import PIL

'''
the gui:
BUTTONS AREA:
Image file: [open file, open url, save, save as: jpeg, png, tiff, others],
Edit image: [crop, flip, rotate, resize],
Colors: [color_balance, contrast, COL_to_BW, brightness, sharpness, noise]
Filters: [blur, contour, edge_enhance, emboss, unsharp, smooth]
IMAGE AREA:
SLIDERS AREA: [save to image butt(closes slider), ]
'''

root = tk.Tk()
root.title('Image Editor')
root.geometry('1080x810')
root.resizable(False, False)

def buttons_placement_field(main):
    backgr = 'green'
    filling = 'both'
    exp = True
    def f(x_, y_, width_, height_):  # 
        field = tk.Frame(master=main, background=backgr)
        field.pack(expand=exp, fill=filling)
        field.place(x=x_,y=y_, width=width_, height=height_)
        return field
    return f

def buttons(main):
    backgr = 'dark green'
    exp=False
    filling ='none'
    side_= 'left'
    def f(x_:int, y_:int, width_:int, txt:str, comm):
        button = tk.Button(master=main, text=txt, command=comm, background=backgr)
        button.pack(expand=exp, fill=filling, side=side_)
        button.place(x=x_, y=y_, width=width_)
        return button
    return f

def fake():
    pass

def file_buttons():
    # file buttons place
    file_button_field = button_field(x_=40, y_=60, width_=100, height_=135)
    
    # file buttons
    f_buttons = buttons(file_button_field)
    f_buttons(
        x_=6, y_=10, width_=85, txt='Open file', 
        comm=lambda: [fake(), file_button_field.destroy()])  # file_open = 
    f_buttons(
        x_=6, y_=40, width_=85,txt='Open url', 
        comm=lambda: [fake(), file_button_field.destroy()])  # file_open_url = 
    f_buttons(
        x_=6, y_=70, width_=85, txt='Save', 
        comm=lambda: [fake(), file_button_field.destroy()])  # file_save = 
    f_buttons(
        x_=6, y_=100, width_=85, txt='Save as', 
        comm=lambda: [fake(), file_button_field.destroy()])  # file_save_as = 

def edit_buttons():
    # edit buttons place
    edit_button_field = button_field(x_=150, y_=60, width_=100, height_=135)

    # edit buttons
    e_buttons = buttons(edit_button_field)
    e_buttons(
        x_=6, y_=10, width_=85, txt='Crop image', 
        comm=lambda: [fake(), edit_button_field.destroy()])  # edit_crop = 
    e_buttons(
        x_=6, y_=40, width_=85, txt='Flip image', 
        comm=lambda: [fake(), edit_button_field.destroy()])  # edit_flip = 
    e_buttons(
        x_=6, y_=70, width_=85, txt='Rotate', 
        comm=lambda: [fake(), edit_button_field.destroy()])  # edit_rotate = 
    e_buttons(
        x_=6, y_=100, width_=85, txt='Resize', 
        comm=lambda: [fake(), edit_button_field.destroy()])  # edit_resize = 


def color_buttons():
    # color buttons place
    color_button_field = button_field(x_=260, y_=60, width_=100, height_=195)

    # color buttons
    color_buttons = buttons(color_button_field)
    color_buttons(
        x_=6, y_=10, width_=85, txt='Color Balance', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_balance = 
    color_buttons(
        x_=6, y_=40, width_=85, txt='Contrast', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_contrast = 
    color_buttons(
        x_=6, y_=70, width_=85, txt='Destaturate', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_COL_to_BW = 
    color_buttons(
        x_=6, y_=100, width_=85, txt='Brightness', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_brightness = 
    color_buttons(
        x_=6, y_=130, width_=85, txt='Sharpness', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_sharpness = 
    color_buttons(
        x_=6, y_=160, width_=85, txt='Color Noise', 
        comm=lambda: [fake(), color_button_field.destroy()])  # color_noise = 

def filter_buttons():
    # filter buttons place
    filter_button_field = button_field(x_=370, y_=60, width_=100, height_=195)

    # filter buttons
    filter_buttons = buttons(filter_button_field)
    filter_buttons(
        x_=6, y_=10, width_=85, txt='Blur', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_blur = 
    filter_buttons(
        x_=6, y_=40, width_=85, txt='Contour', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_contour = 
    filter_buttons(
        x_=6, y_=70, width_=85, txt='Edge Enhance', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_edge_enhance = 
    filter_buttons(
        x_=6, y_=100, width_=85, txt='Emboss', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_emboss = 
    filter_buttons(
        x_=6, y_=130, width_=85, txt='Unsharp', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_unsharp = 
    filter_buttons(
        x_=6, y_=160, width_=85, txt='Smooth', 
        comm=lambda: [fake(), filter_button_field.destroy()])  # filter_smooth = 

# buttons place
button_field = buttons_placement_field(root)

# top buttons place
top_button_field = button_field(x_=30, y_=19, width_=1010, height_=40)

# top buttons
top_buttons = buttons(top_button_field)
file = top_buttons(x_=10, y_=6, width_=100, txt='File', comm=lambda: [file_buttons()])
edit = top_buttons(x_=120, y_=6, width_=100, txt='Edit', comm=edit_buttons)
colors = top_buttons(x_=230, y_=6, width_=100, txt='Colors', comm=color_buttons)
filters = top_buttons(x_=340, y_=6, width_=100, txt='Filters', comm=filter_buttons)

# image
image_field = tk.Frame(root, background='red')  # , text='image'
image_field.pack(expand=True, fill='both')
image_field.place(relx=0.217, rely=0.1, relwidth=0.75, relheight=0.6)

# # sliders
# sliders_field = tk.Frame(root, background='yellow')  # , text='sliders'
# sliders_field.pack(expand=True, fill='both')
# sliders_field.place(relx=0.217, rely=0.72, relwidth=0.75, relheight=0.25)

root.mainloop()