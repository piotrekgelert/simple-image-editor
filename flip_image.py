import tkinter as tk


class FlipImage:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Flip image')
        top.geometry('400x100')
        self.update = update
        self.flip_dict = {'vertical': 0, 'horizont': 0}
        
        button_flip = self.flip_button(top)
        button_flip(
            'Flip image horizontally',
            lambda:[self.horizont_flip(), top.destroy()],
            10, 20, 380, 30)
        button_flip('Flip image vertically',
                    lambda:[self.vertical_flip(), top.destroy()],
                    10, 60, 380, 30)
    
    def flip_button(self, main):
        def f(txt, comm, x_, y_, width_, height_):
            button = tk.Button(main, text=txt, command=comm)
            button.pack()
            button.place(x=x_, y=y_, width=width_, height=height_)
            return button
        return f
    
    def horizont_flip(self):
        self.flip_dict['horizont'] = 1
        self.update(self.flip_dict)
    
    def vertical_flip(self):
        self.flip_dict['vertical'] = 1
        self.update(self.flip_dict)