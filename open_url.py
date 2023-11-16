import tkinter as tk

from utils import Utils


class OpenUrlImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Open image from url')
        top.geometry('400x300')
        self.update = update

        ulabel = tk.Label(top, text='Insert link url:')  # , font=('arial', 12)
        ulabel.pack()
        ulabel.place(x=10, y=5)  # , width=370, height=0.3

        self.textfield = tk.Entry(top)  # , font=('arial', 12)
        self.textfield.pack(expand=True, fill='x')
        self.textfield.place(x=10, y=26, width=350, height=25)  # 
        self.textfield.focus()
        
        button = self.buttons(top)
        button('Open link', lambda: [self.submit(), top.destroy()],
               10, 60, 100, 30)
        button('Open selected link',
               lambda:[self.submit_recent(), top.destroy()], 10, 260)
        
        label = self.labels(top)
        label('Recent url links:', 10, 110)

        self.recent_field = tk.Listbox(top)
        self.recent_field.pack()
        self.recent_field.place(x=10, y=130, width=350, height=120)

        self.recent_ls = []
        with open('recent_url_paths.txt', 'r') as f:
            for file in f.readlines():
                self.recent_field.insert(tk.END, file)
                self.recent_ls.insert(0, file)

    def submit(self):
        path_a = self.textfield.get()
        with open('recent_url_paths.txt', 'a') as f:
            f.write(path_a)  #  + '\n'
        self.update(path_a)
    
    def submit_recent(self):
        recent_url = self.recent_field.curselection()[0]
        path_a = self.recent_ls[recent_url]
        self.update(path_a)