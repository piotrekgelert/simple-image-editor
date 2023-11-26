import tkinter as tk

from utils import Utils


class FlipImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field']
        )
        top.title('Flip image')
        top.geometry('400x100')
        self.update = update
        self.flip_dict = {'vertical': 0, 'horizont': 0}
        
        button = self.buttons(top)
        button(
            'Flip image horizontally',
            lambda:[self.horizont_flip(), top.destroy()],
            10, 20, 380, 30)
        button('Flip image vertically',
                    lambda:[self.vertical_flip(), top.destroy()],
                    10, 60, 380, 30)

    
    def horizont_flip(self):
        self.flip_dict['horizont'] = 1
        self.update(self.flip_dict)
    
    def vertical_flip(self):
        self.flip_dict['vertical'] = 1
        self.update(self.flip_dict)