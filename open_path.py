import os
import tkinter as tk

from utils import Utils


class OpenImageSelector(Utils):
    def __init__(self , update_a, update_b= None):  #
        top = tk.Toplevel(background=self.app_colors()['color_butt_place_field'])
        top.title('Select method to open the image')
        top.geometry('400x400')
        self.update_a = update_a
        self.update_b = update_b
        drives = [
            f'{chr(x)}' for x in range(61, 91)\
                if os.path.exists(f'{chr(x)}:\\')]

        drives_label_txt = '''Choose one or more hard drives from available list: {}
        (more drives, longer search for images), 
        >> insert example: c, d, e <<'''

        label = self.labels(top)
        label(drives_label_txt.format(drives), 20, 3)
        label('Insert link to the chosen folder with images', 20 , 140)
        label('Paths to the recently opened folders', 20, 240)

        button = self.buttons(top)
        button('Submit hard drive(s)',
               lambda: [self.submit_drive() , top.destroy()], 20, 90)
        button('Submit path',
               lambda: [self.submit_folder(), top.destroy()], 20, 190)
        button('Submit selected path',
               lambda:[self.submit_recent(), top.destroy()], 20, 365)
        
        entry = self.entries(top)
        self.drives_field = entry(20, 60, 360, 25)
        self.folder_field = entry(20, 160, 360, 25)

        listbox = self.listboxes(top)
        self.recent_field = listbox(20, 260, 360, 100)

        self.recent_ls = []
        with open('recent_comp_paths.txt', 'r') as f:
            for recent_file in f.readlines():
                rc = '\\'.join(recent_file.split('\\')[:-2])
                # rr = recent_file.split('\\')[:-2]
                # print(rr, recent_file)
                # print(self.recent_field.get())
                self.recent_ls.insert(0, rc)
                self.recent_field.insert(0, rc)
    
    def submit_folder(self):
        path_folder = self.folder_field.get()
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_folder+ '\n')  #  
        OpenPathImage(self.update_a, path_folder)
    
    def submit_drive(self):
        path_drive = self.drives_field.get()
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_drive)  #  + '\n'
        OpenPathImage(self.update_a, path_drive)
    
    def submit_recent(self):
        recent_idx = self.recent_field.curselection()[0]
        OpenPathImage(self.update_a, self.recent_ls[recent_idx])


class OpenPathImage(Utils):
    def __init__(self, update_a, update_b):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title('Open image from path')
        top.geometry('600x800')
        self.update_a = update_a
        self.update_b = update_b

        label = self.labels(top)
        label('Paths to images (search on all avaible hard drives):', 10, 5)

        self.imbox = tk.Listbox(top)
        self.imbox.pack()
        self.imbox.place(x=10, y=25, width=580, height=700)

        button = self.buttons(top)
        button('Load selected image path',
               lambda:[self.submit(), top.destroy()], 10, 750, 200, 30)

        # avaible_hard_drives = [f'{chr(x)}:\\' for x in range(61, 91)\
        #                        if os.path.exists(f'{chr(x)}')]
        # processors_num = os.cpu_count()
        # with ThreadPoolExecutor(max_workers=processors_num) as proc:
        #     self.im_files = proc.map(self.find_images(avaible_hard_drives))
        
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
        print(path_a)
        self.update_a(path_a)
        with open('recent_comp_paths.txt', 'a') as f:
            f.write('\n' + path_a)  #  
        