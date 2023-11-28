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
        label('File name (default:"image"):', 10, 25)
        label('Image format: jpg, png, tiff (default: original format)', 10, 80)  # 75
        label('Path to save the image (default: Documents path)', 10, 135)  # 125

        field = self.entries(top)
        self.file_name = field(10, 45, 300, 25)
        self.file_extension = field(10, 100, 50, 25)  # 95
        self.file_path = field(10, 155, 300, 25)  # 145

        button = self.buttons(top)
        button('Save as', top.destroy, x_=80, y_=200, width_=100, height_=25)
        button('Cancel', lambda: [self.cancel(), top.destroy()], x_=200, y_=200, width_=100, height_=25)
        button('test', self.submit, x_=320, y_=200, width_=100, height_=25)


    def submit(self):
        self.file['cancel'] = '0'
        self.file['name'] = self.file_name.get()
        self.file['extension'] = self.file_extension.get()
        self.file['path'] = self.file_path.get()
        self.update(self.file)
    
    def cancel(self):
        self.file['cancel'] = '1'
        self.update(self.file)


class NameImageFind:
    pass