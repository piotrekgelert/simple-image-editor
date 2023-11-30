import tkinter as tk
from collections import defaultdict

from utils import Utils


class RotateImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field']
        )
        top.title('Rotate image')
        top.geometry('400x300')
        self.update = update
        self.rot = {}
        
        button = self.buttons(top)
        button('Rotate image by 90 degrees', self.rotate_90,
                40, 20, 320, 30)
        button('Rotate image by 180 degrees', self.rotate_180,
                40, 60, 320, 30)
        button('Rotate image by 270 degrees',self.rotate_270,
                40, 100, 320, 30)
        button('Rotate image by custom angle', self.rotate_custom,
                40, 210, 320, 30)
        button('Cancel',
               lambda: [self.cancel(), top.destroy()],
               40, 250, 150, 30)
        button('Apply&Exit', lambda: [self.apply(), top.destroy()],
               210, 250, 150, 30)
        
        

        label = self.labels(top)
        label('Choose own amount of degrees:', 40, 150)
        
        entry = self.entries(top)
        self.custom_rot_entry = entry(40, 175, 100, 25)

    def _rotate(self, rot:str, num:int):
        lst = ['rot90', 'rot180', 'rot270', 'rot_cust', 'apply', 'cancel']
        [self.rot.update({x: num}) if x == rot else self.rot.update({x: 0}) for x in lst]
        self.update(self.rot)
        
    def rotate_90(self):
        self._rotate('rot90', 90)

    def rotate_180(self):
        self._rotate('rot180', 180)
    
    def rotate_270(self):
        self._rotate('rot270', 270)

    def rotate_custom(self):
        self._rotate('rot_cust', int(self.custom_rot_entry.get()))

    def cancel(self):
        self._rotate('cancel', 1)

    def apply(self):
        self.rot['apply'] = 1
        self.update(self.rot)
