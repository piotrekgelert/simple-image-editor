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

# top buttons place
top_button_field = tk.Frame(root, background='green')  # , text= 'buttons'
top_button_field.pack(expand=True, fill='both')
top_button_field.place(x=30, y=19, width=1010, height=40)

# top buttons
file = tk.Button(top_button_field, text='File', background='dark green')
file.pack(expand=False, fill='none', side='left')
file.place(x=10, y=6, width=100)

edit = tk.Button(top_button_field, text='Edit', background='dark green')
edit.pack(expand=False, fill='none', side='left')
edit.place(x=120, y=6, width=100)

colors = tk.Button(top_button_field, text='Colors', background='dark green')
colors.pack(expand=False, fill='none', side='left')
colors.place(x=230, y=6, width=100)

filters = tk.Button(top_button_field, text='Filters', background='dark green')
filters.pack(expand=False, fill='none', side='left')
filters.place(x=340, y=6, width=100)


#side buttons place
side_button_field = tk.Frame(root, background='green')  # , text= 'buttons'
side_button_field.pack(expand=True, fill='both')
side_button_field.place(x=40, y=60, width=100, height=150)

# side buttons
file_open = tk.Button(side_button_field, text= 'Open file', background='dark green')
file_open.pack(expand=False, fill='none')
file_open.place(x=6, y=10, width=85)

file_open_url = tk.Button(side_button_field, text= 'Open url', background='dark green')
file_open_url.pack(expand=False, fill='none')
file_open_url.place(x=6, y=40, width=85)

file_save = tk.Button(side_button_field, text= 'Save', background='dark green')
file_save.pack(expand=False, fill='none')
file_save.place(x=6, y=70, width=85)

file_save_as = tk.Button(side_button_field, text= 'Save as', background='dark green')
file_save_as.pack(expand=False, fill='none')
file_save_as.place(x=6, y=100, width=85)

# image
image_field = tk.Frame(root, background='red')  # , text='image'
image_field.pack(expand=True, fill='both')
image_field.place(relx=0.217, rely=0.1, relwidth=0.75, relheight=0.6)

# sliders
sliders_field = tk.Frame(root, background='yellow')  # , text='sliders'
sliders_field.pack(expand=True, fill='both')
sliders_field.place(relx=0.217, rely=0.72, relwidth=0.75, relheight=0.25)

root.mainloop()