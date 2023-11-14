import tkinter as tk


class FlipImage:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Flip image')
        top.geometry('400x100')
        self.update = update
        self.flip_dict = {'vertical': 0, 'horizont': 0}
        
        button_horizont = tk.Button(
            top, text='Flip image horizontally',
            command=lambda:[self.horizont_flip(), top.destroy()])
        button_horizont.pack()
        button_horizont.place(x=10, y=20, width=380, height=30)

        button_vertical = tk.Button(
            top, text='Flip image vertically',
            command=lambda:[self.vertical_flip(), top.destroy()])
        button_vertical.pack()
        button_vertical.place(x=10, y=60, width=380, height=30)
    
    def horizont_flip(self):
        self.flip_dict['horizont'] = 1
        self.update(self.flip_dict)
    
    def vertical_flip(self):
        self.flip_dict['vertical'] = 1
        self.update(self.flip_dict)

    
        
