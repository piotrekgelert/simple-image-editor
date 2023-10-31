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
    def f(x_:int, y_:int, width_:int, txt:str):
        button = tk.Button(master=main, text=txt, background=backgr)
        button.pack(expand=exp, fill=filling, side=side_)
        button.place(x=x_, y=y_, width=width_)
        return button
    return f

# buttons place
button_field = buttons_placement_field(root)

# top buttons place
top_button_field = button_field(x_=30, y_=19, width_=1010, height_=40)

# top buttons
top_buttons = buttons(top_button_field)
file = top_buttons(x_=10, y_=6, width_=100, txt='File')
edit = top_buttons(x_=120, y_=6, width_=100, txt='Edit')
colors = top_buttons(x_=230, y_=6, width_=100, txt='Colors')
filters = top_buttons(x_=340, y_=6, width_=100, txt='Filters')

# file buttons place
file_button_field = button_field(x_=40, y_=60, width_=100, height_=135)

# file buttons
file_buttons = buttons(file_button_field)
file_open = file_buttons(x_=6, y_=10, width_=85, txt='Open file')
file_open_url = file_buttons(x_=6, y_=40, width_=85, txt='Open url')
file_save = file_buttons(x_=6, y_=70, width_=85, txt='Save')
file_save_as = file_buttons(x_=6, y_=100, width_=85, txt='Save as')

# edit buttons place
edit_button_field = button_field(x_=150, y_=60, width_=100, height_=135)

# edit buttons
edit_buttons = buttons(edit_button_field)
edit_crop = edit_buttons(x_=6, y_=10, width_=85, txt='Crop image')
edit_flip = edit_buttons(x_=6, y_=40, width_=85, txt='Flip image')
edit_rotate = edit_buttons(x_=6, y_=70, width_=85, txt='Rotate')
edit_resize = edit_buttons(x_=6, y_=100, width_=85, txt='Resize')

# color buttons place
color_button_field = button_field(x_=260, y_=60, width_=100, height_=195)

# color buttons
color_buttons = buttons(color_button_field)
color_balance = color_buttons(x_=6, y_=10, width_=85, txt='Color Balance')
color_contrast = color_buttons(x_=6, y_=40, width_=85, txt='Contrast')
color_COL_to_BW = color_buttons(x_=6, y_=70, width_=85, txt='Destaturate')
color_brightness = color_buttons(x_=6, y_=100, width_=85, txt='Brightness')
color_sharpness = color_buttons(x_=6, y_=130, width_=85, txt='Sharpness')
color_noise = color_buttons(x_=6, y_=160, width_=85, txt='Color Noise')

# filter buttons place
filter_button_field = button_field(x_=370, y_=60, width_=100, height_=195)

# filter buttons
filter_buttons = buttons(filter_button_field)
filter_blur = filter_buttons(x_=6, y_=10, width_=85, txt='Blur')
filter_contour = filter_buttons(x_=6, y_=40, width_=85, txt='Contour')
filter_edge_enhance = filter_buttons(x_=6, y_=70, width_=85, txt='Edge Enhance')
filter_emboss = filter_buttons(x_=6, y_=100, width_=85, txt='Emboss')
filter_unsharp = filter_buttons(x_=6, y_=130, width_=85, txt='Unsharp')
filter_smooth = filter_buttons(x_=6, y_=160, width_=85, txt='Smooth')

# image
# image_field = tk.Frame(root, background='red')  # , text='image'
# image_field.pack(expand=True, fill='both')
# image_field.place(relx=0.217, rely=0.1, relwidth=0.75, relheight=0.6)

# sliders
sliders_field = tk.Frame(root, background='yellow')  # , text='sliders'
sliders_field.pack(expand=True, fill='both')
sliders_field.place(relx=0.217, rely=0.72, relwidth=0.75, relheight=0.25)

root.mainloop()