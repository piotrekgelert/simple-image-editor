import os
import tkinter as tk


class OpenImageSelector:
    def __init__(self , update_a, update_b= None):  #
        top = tk.Toplevel()
        top.title('Select method to open the image')
        top.geometry('400x400')
        self.update_a = update_a
        self.update_b = update_b
        drives = [f'{chr(x)}' for x in range(61, 91) if os.path.exists(f'{chr(x)}:\\')]
        # print(drives)
        drives_label_txt = '''Choose one or more hard drives from available list: {}
        (more drives, longer search for images), 
        >> insert example: c, d, e <<'''
        drives_label = tk.Label(
            top,
            text=drives_label_txt.format(drives))
        drives_label.pack()
        drives_label.place(x=20, y=3)

        self.drives_field = tk.Entry(top)
        self.drives_field.pack()
        self.drives_field.place(x=20, y=60, height=25, width=360)

        drives_button = tk.Button(
            top,
            text='Submit hard drive(s)',
            command=lambda: [self.submit_drive() , top.destroy()])
        drives_button.pack()
        drives_button.place(x=20, y=90)

        folder_label = tk.Label(
            top,
            text='Insert link to the chosen folder with images')
        folder_label.pack()
        folder_label.place(x=20 , y=140)

        self.folder_field = tk.Entry(top)
        self.folder_field.pack()
        self.folder_field.place(x=20, y=160, height=25, width=360)

        folder_button = tk.Button(
            top,
            text= 'Submit path',
            command=lambda: [self.submit_folder(), top.destroy()]  # , self.open_image_path()
        )
        folder_button.pack()
        folder_button.place(x=20, y=190)
        
        resent_label = tk.Label(top, text='Paths to the recently opened folders')
        resent_label.pack()
        resent_label.place(x=20, y=240)

        self.recent_field = tk.Listbox(top)
        self.recent_field.pack()
        self.recent_field.place(x=20, y=260, width=360, height=100)

        recent_button = tk.Button(
            top,
            text='Submit selected path',
            command=lambda:[self.submit_recent(), top.destroy()])
        recent_button.pack()
        recent_button.place(x=20, y=365)

        self.recent_ls = []
        with open('recent_comp_paths.txt', 'r') as f:
            for recent_file in f.readlines():
                rc = '\\'.join(recent_file.split('\\')[:-2])
                self.recent_ls.insert(0, rc)
                self.recent_field.insert(0, rc)

    def submit_folder(self):
        path_folder = self.folder_field.get()
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_folder)  #  + '\n'
        OpenPathImage(self.update_a, path_folder)
    
    def submit_drive(self):
        path_drive = self.drives_field.get()
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_drive)  #  + '\n'
        OpenPathImage(self.update_a, path_drive)
    
    def submit_recent(self):
        recent_idx = self.recent_field.curselection()[0]
        OpenPathImage(self.update_a, self.recent_ls[recent_idx])


class OpenPathImage:
    def __init__(self, update_a, update_b):
        top = tk.Toplevel()
        top.title('Open image from path')
        top.geometry('600x800')
        self.update_a = update_a
        self.update_b = update_b

        llabel = tk.Label(
            top, 
            text='Paths to images (search on all avaible hard drives):')
        llabel.pack()
        llabel.place(x= 10, y=5)

        self.imbox = tk.Listbox(top)
        self.imbox.pack()
        self.imbox.place(x=10, y=25, width=580, height=700)

        imbutton = tk.Button(top, text='Load selected image path',
                             command=lambda:[self.submit(), top.destroy()])
        imbutton.pack()
        imbutton.place(x=10, y=750, width=200, height=30)

        # avaible_hard_drives = [f'{chr(x)}:\\' for x in range(61, 91)\
        #                        if os.path.exists(f'{chr(x)}')]
        # processors_num = os.cpu_count()
        # with ThreadPoolExecutor(max_workers=processors_num) as proc:
        #     self.im_files = proc.map(self.find_images(avaible_hard_drives))
        
        # print(self.update_b)
        if '\\' in self.update_b:
            self.im_files = self.find_images([self.update_b])
        else:
            res=[f'{x.upper()}:\\' for x in self.update_b.split(',')]
            # print(res)
            self.im_files = self.find_images(res)
        for x in self.im_files:
            self.imbox.insert(tk.END, x.split('\\')[-1])
    
    def find_images(self, im_drives):
        f_im = []
        for drive in im_drives:
            for r, d, files in os.walk(drive):
                for fl in files:
                    if fl.endswith('.jpg') or fl.endswith('.png'):  # 
                        f_im.append(f'{r}\\\{fl}')
        return f_im
    
    def submit(self):
        img_idx = self.imbox.curselection()[0]
        path_a = self.im_files[img_idx]
        with open('recent_comp_paths.txt', 'a') as f:
            f.write(path_a)  #  + '\n'
        self.update_a(path_a)