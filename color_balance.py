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
        top.geometry('400x200')
        self.update = update

        label = self.labels(top)
        label('Adjust image color balance. \n \
        An enhancement factor of 0.0 gives a black and white image.\n \
        A factor of 1.0 gives the original image', 10, 25)

        self.slider = tk.Scale(
            top, from_=0.0, to=1.0,
            tickinterval=1, resolution=0.01, length=370,
            orient='horizontal')
            # command=self.get_slider_value)
        self.slider.pack()
        self.slider.place(x=10, y=80)

        button = self.buttons(top)
        button('Apply', self.submit, 40, 150, 100, 30)
        button('Reset', self.reset_slider_value, 150, 150, 100, 30)
        button('Cancel', top.destroy, 260, 150, 100, 30)
    
    # def get_slider_value(self, val):
    #     return val
        # ls = []
        # ls.append(float(val))
        # print(ls)
        # # self.update(val)
        # # print(val)
    
    def reset_slider_value(self):
        self.update(1.0)
    
    def submit(self):
        val = self.slider.get()
        # self.get_slider_value
        # print(val)
        self.update(float(val))