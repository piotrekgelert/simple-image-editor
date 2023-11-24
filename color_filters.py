'''
https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html
https://python-course.eu/tkinter/sliders-in-tkinter.php
https://pythonbasics.org/tkinter-scale/
https://www.codeunderscored.com/tkinter-scrollbar-explained-with-examples/
https://stackoverflow.com/questions/59166448/whats-the-formula-used-in-pil-imageenhance-enhance-feature-for-color-brightnes
'''
import tkinter as tk

from utils import Utils


class ColorFiltersUpto1(Utils):
    def __init__(self, update, tiltle, label_txt):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title(tiltle)
        top.geometry('400x200')
        self.update = update
        self.upd_val = 1

        label = self.labels(top)
        label(label_txt, 10, 25)
        
        self.slider = tk.Scale(
            top, background=self.app_colors()['color_butt_place_field'],
            from_= 0.0, to=1.0,
            tickinterval=1, resolution=0.01, length=370,
            orient='horizontal')
        self.slider.pack()
        self.slider.place(x=10, y=80)

        button = self.buttons(top)
        button('Submit', self.submit, 25, 150, 90, 30)
        button('Cancel', 
               lambda: [self.reset_slider_value(), top.destroy()],
               125, 150, 90, 30)
        button(
            'Apply changes & Exit',
            lambda: [self.apply_changes(), top.destroy()], 225, 150, 150, 30)
    
    def reset_slider_value(self):
        self.update([self.upd_val, 1.0])
    
    def submit(self):
        val = self.slider.get()
        self.update([self.upd_val, float(val)])
    
    def apply_changes(self):
        self.upd_val = 0
        val = self.slider.get()
        self.update([self.upd_val, float(val)])


class ColorFiltersUpto2(Utils):
    def __init__(self, update, tiltle, label_txt):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title(tiltle)
        top.geometry('400x200')
        self.update = update
        self.upd_val = 1

        label = self.labels(top)
        label(label_txt, 10, 15)
        
        self.slider = tk.Scale(
            top, 
            background=self.app_colors()['color_butt_place_field'],
            from_= 0.0, to=2.0,
            tickinterval=1, resolution=0.01, length=370,
            orient='horizontal')
        self.slider.pack()
        self.slider.place(x=10, y=80)

        button = self.buttons(top)
        button('Submit', self.submit, 25, 150, 90, 30)
        button('Cancel', 
               lambda: [self.reset_slider_value(), top.destroy()],
               125, 150, 90, 30)
        button(
            'Apply changes & Exit',
            lambda: [self.apply_changes(), top.destroy()], 225, 150, 150, 30)
    
    def reset_slider_value(self):
        self.update([self.upd_val, 1.0])
    
    def submit(self):
        val = self.slider.get()
        self.update([self.upd_val, float(val)])
    
    def apply_changes(self):
        self.upd_val = 0
        self.update([self.upd_val])