import tkinter as tk


class Utils:
    def buttons(self, main):
        def f(txt, comm, x_, y_):
            button = tk.Button(master=main, text=txt, command=comm)
            button.pack()
            button.place(x=x_, y=y_)
            return button
        return f
    
    def labels(self, main):
        def f(txt, x_, y_):
            label = tk.Label(master=main, text=txt)
            label.pack()
            label.place(x=x_, y=y_)
            return label
        return f
    
    def entries(self, main):
        def f(x_, y_, width_, height_):
            entry = tk.Entry(main)
            entry.pack()
            entry.place(x=x_, y=y_, width=width_, height=height_)
            return entry
        return f