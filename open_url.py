import tkinter as tk

from utils import Utils


class OpenUrlImage(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title('Open image from url')
        top.geometry('400x300')
        self.update = update

        label = self.labels(top)
        label('Insert link url:', 10, 5)
        label('Recent url links:', 10, 110)
        
        txtfield = self.entries(top)
        self.textfield = txtfield(10, 26, 350, 25)
        
        button = self.buttons(top)
        button('Open link', lambda: [self.submit(), top.destroy()],
               10, 60, 100, 30)
        button('Open selected link',
               lambda:[self.submit_recent(), top.destroy()], 10, 260)
        
        lstbox = self.listboxes(top)
        self.recent_field = lstbox(10, 130, 350, 120)

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