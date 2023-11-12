import tkinter as tk


class CropImage:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title()
        top.geometry('400x400')
        self.update = update

        left_txt = tk.Label(top,text='Old left edge to the new left:')
        left_txt.pack()
        left_txt.place(x=10, y=30)
        self.left_input = tk.Entry(top)
        self.left_input.pack()
        self.left_input.place(x=10, y=50, width=150, height=20)

        upper_txt = tk.Label(top,text='Old top edge to the new top:')
        upper_txt.pack()
        upper_txt.place(x=180, y=30)
        self.upper_input = tk.Entry(top)
        self.upper_input.pack()
        self.upper_input.place(x=180, y=50, width=150, height=20)

        right_txt = tk.Label(top,text='Old left edge to the new right:')
        right_txt.pack()
        right_txt.place(x=10, y=80)
        self.right_input = tk.Entry(top)
        self.right_input.pack()
        self.right_input.place(x=10, y=100, width=150, height=20)

        lower_txt = tk.Label(top,text='Old top edge to the new bottom:')
        lower_txt.pack()
        lower_txt.place(x=180, y=80)
        self.lower_input = tk.Entry(top)
        self.lower_input.pack()
        self.lower_input.place(x=180, y=100, width=150, height=20)

        apply_button = tk.Button(
            top, text='Apply changes',
            command=self.submit_apply
        )
        apply_button.pack()
        apply_button.place(x=10, y=130, width=100)
        cancel_button = tk.Button(
            top, text= 'Cancel',
            command=lambda: [self.submit_cancel(), top.destroy()]
        )
        cancel_button.pack()
        cancel_button.place(x=130, y=130, width=100)
        exit_button = tk.Button(
            top, text='Exit',
            command=lambda:[self.submit_exit(), top.destroy()]
        )
        exit_button.pack()
        exit_button.place(x=260, y=130, width=100)

    def submit_apply(self):
        cancel=False
        new_dimensions = (
            cancel,
            int(self.left_input.get()),
            int(self.upper_input.get()),
            int(self.right_input.get()),
            int(self.lower_input.get())
            )
        self.update(new_dimensions)
    
    def submit_cancel(self):
        cancel=True
        new_dimensions = (cancel, 0, 0, 0, 0)
        self.update(new_dimensions)

    def submit_exit(self):
        pass