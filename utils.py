import tkinter as tk


class Utils:
    def buttons(self, main):
        def f(txt:str, comm, x_:int, y_:int, width_:int=None, height_:int=None):
            button = tk.Button(master=main, text=txt, command=comm)
            button.pack()
            if (width_ and height_) is not None:
                button.place(x=x_, y=y_, width=width_, height=height_)
            else:
                button.place(x=x_, y=y_)
            return button
        return f
    
    def labels(self, main):
        def f(txt:str, x_:int, y_:int):
            label = tk.Label(master=main, text=txt)
            label.pack()
            label.place(x=x_, y=y_)
            return label
        return f
    
    def entries(self, main):
        def f(x_:int, y_:int, width_:int, height_:int):
            entry = tk.Entry(main)
            entry.pack()
            entry.place(x=x_, y=y_, width=width_, height=height_)
            return entry
        return f