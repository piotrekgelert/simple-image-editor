import tkinter as tk

from utils import Utils


class ResizeImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Resize image')
        top.geometry('360x240')
        self.update = update
    
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
        button('Interpolation', self.interpolation, 80, 150, 100, 25)
        button('Reset', self.reset, 10, 200, 100, 25)
        button('Resize', self.resize, 130, 200, 100, 25)
        button('Cancel', self.cancel, 250, 200, 100, 25)
    

    def interpolation(self):
        pass

    def reset(self):
        pass

    def resize(self):
        pass

    def cancel(self):
        pass
    
