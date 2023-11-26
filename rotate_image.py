import tkinter as tk

from utils import Utils


class RotateImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field']
        )
        top.title('Rotate image')
        top.geometry('400x400')
        self.update = update
        
        button = self.buttons(top)
        button('Rotate image by 90 degrees',
                lambda: [self.rotate_90(), top.destroy()],
                40, 20, 320, 30)
        button('Rotate image by 180 degrees',
                lambda: [self.rotate_180(), top.destroy()],
                40, 60, 320, 30)
        button('Rotate image by 270 degrees',
                lambda: [self.rotate_270(), top.destroy()],
                40, 100, 320, 30)
        button('Rotate',
                lambda: [self.rotate_custom(), top.destroy()],
                40, 240, 320, 30)

        label = self.labels(top)
        label('Choose own amount of degrees:', 40, 180)
        
        entry = self.entries(top)
        self.custom_rot_entry = entry(40, 205, 100, 25)

    
    def rotate_90(self):
        self.update('90')

    def rotate_180(self):
        self.update('180')
    
    def rotate_270(self):
        self.update('270')

    def rotate_custom(self):
        self.update(self.custom_rot_entry.get())
