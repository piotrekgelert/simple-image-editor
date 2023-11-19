import tkinter as tk

from utils import Utils


class ResizeImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Resize image')
        top.geometry('360x240')
        self.update = update
        self.interpol = None
    
        label = self.labels(top)
        label('Image Size:', 10, 20)
        label('Width:', 20, 50)
        label('px', 190, 50)
        label('Hight:', 20, 100)
        label('px', 190, 100)
        label('Quality:', 10, 150)

        entry = self.entries(top)
        self.im_width = entry(80, 45, 100, 30)
        self.im_heigh = entry(80, 95, 100, 30)

        button = self.buttons(top)
        button('Interpolation', self.interpolation_class, 80, 150, 100, 25)
        button(
            'Reset',
            lambda: self.reset(), 10, 200, 100, 25)
        button(
            'Resize', 
            lambda: [self.resize(), top.destroy()], 130, 200, 100, 25)
        button(
            'Cancel',
            lambda: [self.cancel(), top.destroy()], 250, 200, 100, 25)
    

    def interpolation_class(self):
        Interpolation(self.interpolation)

    def interpolation(self, upd):
        self.interpol = upd

    def reset(self):
        self.im_width.delete(0, 'end')
        self.im_heigh.delete(0, 'end')
        self.interpol = None

    def resize(self):
        if self.interpol:
            resize_list = [
                int(self.im_width.get()), int(self.im_heigh.get()), self.interpol
        ]
        else:
            resize_list = [
                int(self.im_width.get()), int(self.im_heigh.get())
        ] 
        self.update(resize_list) 

    def cancel(self):
        pass



class Interpolation(Utils):
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Interpolation')
        top.geometry('260x200')
        self.update = update
        self.filters = [
            'nearest','box','bilinear','hamming','bicubic','lanchos'
            ]

        label = self.labels(top)
        label('Resample filters:', 10, 20)

        self.textbox = tk.Listbox(top)
        self.textbox.pack()
        self.textbox.place(x=10, y=45, width=240, height=100)

        for x in self.filters:
            self.textbox.insert(tk.END, x)
        
        button = self.buttons(top)
        button(
            'Apply',
            lambda: [self.apply_button(), top.destroy()], 20, 160, 100, 25)
        button(
            'Cancel',
            lambda: [self.cancel_button(), top.destroy()], 140, 160, 100, 25)      
    
    def apply_button(self):
        filter_idx = self.textbox.curselection()[0]
        self.update(self.filters[filter_idx])

    def cancel_button(self):
        pass
