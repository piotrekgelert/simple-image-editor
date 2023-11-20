'''
https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html
https://python-course.eu/tkinter/sliders-in-tkinter.php
https://pythonbasics.org/tkinter-scale/
https://www.codeunderscored.com/tkinter-scrollbar-explained-with-examples/

'''

import tkinter as tk

from utils import Utils


class ColorBalance(Utils):
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Color Balance')
        top.geometry('400x400')
        self.update = update

        label = self.labels(top)
        label('An enhancement factor of 0.0 gives a black and white image.\n \
        A factor of 100.0 gives the original image', 10, 25)

        slider = tk.Scale(
            top, from_=0.0, to=1.0,
            tickinterval=1, resolution=0.01, length=370,
            orient='horizontal',
            command=self.get_slider_value)
        slider.pack()
        slider.place(x=10, y=80)
    
    def get_slider_value(self, val):
        self.update(val)
        # print(val)