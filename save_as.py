import os
import tkinter as tk

from utils import Utils


class SaveAs(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title('Save as')
        top.geometry('400x250')
        self.update = update
        self.file = {}
        
        label = self.labels(top)
        label('REMEMBER!! Result image -> dimensions: 1080x800 (used aspect ratio)', 10, 10)
        label('File name (default:"image"):', 10, 30)
        label('Image format: jpg, png (default: original format)', 10, 85)  # 75
        label('Path to save the image (default: User\Documents path)', 10, 140)  # 125

        field = self.entries(top)
        self.file_name = field(10, 50, 300, 25)
        self.file_extension = field(10, 105, 50, 25)  # 95
        self.file_path = field(10, 160, 300, 25)  # 145

        button = self.buttons(top)
        button('Save as', lambda: [self.submit(), top.destroy()], x_=80, y_=205, width_=100, height_=25)
        button('Cancel', lambda: [self.cancel(), top.destroy()], x_=200, y_=205, width_=100, height_=25)
        # button('test', self.submit, x_=320, y_=200, width_=100, height_=25)


    def submit(self):
        self.file['cancel'] = '0'
        self.file['name'] = self.file_name.get()
        self.file['extension'] = self.file_extension.get()
        self.file['path'] = self.file_path.get()
        self.update(self.file)
    
    def cancel(self):
        self.file['cancel'] = '1'
        self.file['name'] = ''
        self.file['extension'] = ''
        self.file['path'] = ''
        self.update(self.file)