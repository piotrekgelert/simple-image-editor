import tkinter as tk


class RotateImage:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Rotate image')
        top.geometry('400x400')
        self.update = update
        
        buttons = self.rotate_button(top)
        buttons('Rotate image by 90 degrees',
                lambda: [self.rotate_90(), top.destroy()],
                40, 20, 320, 30)
        buttons('Rotate image by 180 degrees',
                lambda: [self.rotate_180(), top.destroy()],
                40, 60, 320, 30)
        buttons('Rotate image by 270 degrees',
                lambda: [self.rotate_270(), top.destroy()],
                40, 100, 320, 30)
        buttons('Rotate',
                lambda: [self.rotate_custom(), top.destroy()],
                40, 240, 320, 30)

        label = tk.Label(top, text='Choose own amount of degrees:')
        label.pack()
        label.place(x=40, y=180)
        
        self.custom_rot_entry = tk.Entry(top)
        self.custom_rot_entry.pack()
        self.custom_rot_entry.place(x=40, y=205, width=100, height=25)

    def rotate_button(self, main):
        def f(txt, comm, x_, y_, width_, height_):
            button = tk.Button(
                main,
                text=txt,
                command=comm)
            button.pack()
            button.place(
                x=x_, y=y_, width=width_, height=height_)
            return button
        return f
    
    def rotate_90(self):
        self.update('90')

    def rotate_180(self):
        self.update('180')
    
    def rotate_270(self):
        self.update('270')

    def rotate_custom(self):
        self.update(self.custom_rot_entry.get())
