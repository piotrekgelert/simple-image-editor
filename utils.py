import tkinter as tk


class Utils:
    def buttons(self, main):
        def f(txt:str, comm, x_:int, y_:int, width_:int=None, height_:int=None):
            button = tk.Button(
                master=main,
                background=self.app_colors()['color_butt'],
                text=txt, command=comm)
            button.pack()
            if (width_ and height_) is not None:
                button.place(x=x_, y=y_, width=width_, height=height_)
            else:
                button.place(x=x_, y=y_)
            return button
        return f
    
    def app_buttons_placement_field(self):
        def f(x_:int, y_:int, width_:int, height_:int):
            field = tk.Frame(
                self, background=self.app_colors()['color_butt_place_field'])
            field.pack(expand=True, fill='both')
            field.place(x=x_,y=y_, width=width_, height=height_)
            return field
        return f
    
    def app_buttons(self, mstr=None):
        colors = self.app_colors()
        def f(x_:int, y_:int, width_:int, txt:str, comm):
            if mstr == None:
                button = tk.Button(
                    master=self, text=txt, command=comm, 
                    background=colors['color_butt'])
            else:
                button = tk.Button(
                    master=mstr, text=txt, command=comm, 
                    background=colors['color_butt'])
            button.pack(expand=False, fill='none', side='left')
            button.place(x=x_, y=y_, width=width_)
            return button
        return f
    
    def labels(self, main):
        def f(txt:str, x_:int, y_:int):
            label = tk.Label(
                master=main, 
                background=self.app_colors()['color_butt_place_field'], 
                text=txt)
            label.pack()
            label.place(x=x_, y=y_)
            return label
        return f
    
    def entries(self, main):
        def f(x_:int, y_:int, width_:int, height_:int):
            entry = tk.Entry(
                main,
                background=self.app_colors()['color_in_field'])
            entry.pack()
            entry.place(x=x_, y=y_, width=width_, height=height_)
            return entry
        return f
    
    def frames(self, main):
        def f(x_, y_, width_, height_):
            fr = tk.Frame(
                main,
                background=self.app_colors()['color_butt_place_field'])
            fr.pack()
            fr.place(x=x_, y=y_, width=width_, height=height_)
            return fr
        return f
    
    def listboxes(self, main):
        def f(x_, y_, width_, height_):
            lstb = tk.Listbox(
                master=main,
                background=self.app_colors()['color_in_field'])
            lstb.pack()
            lstb.place(x=x_, y=y_, width=width_, height=height_)
            return lstb
        return f

    
    def app_colors(self):
        return {
            'color_butt_place_field': '#777777', 
            'color_butt': '#555555',
            'color_in_field': '#BBBBBB'
            }