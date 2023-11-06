import glob
import io
import os
import tkinter as tk
import urllib
from concurrent.futures import ThreadPoolExecutor
from tkinter import filedialog

import PIL
import requests
from PIL import Image, ImageTk

'''
the gui:
BUTTONS AREA:
Image file: [open file, open url, save, save as: jpeg, png, tiff, others],
Edit image: [crop, flip, rotate, resize],
Colors: [color_balance, contrast, COL_to_BW, brightness, sharpness, noise]
Filters: [blur, contour, edge_enhance, emboss, unsharp, smooth]
IMAGE AREA:
SLIDERS AREA: [save to image butt(closes slider), ]
'''


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Image Editor')
        self.geometry('1080x810')
        self.resizable(False, False)
        self.path_ = []
        self.recent_paths_saver()
        self.widgets()

    def recent_paths_saver(self):
        file_comp = 'recent_comp_paths.txt'
        file_url = 'recent_url_paths.txt'
        if (file_comp and file_url) not in os.listdir():
            f_comp = open(file_comp, 'x')
            f_url = open(file_url, 'x')
            f_comp.close()
            f_url.close()
        else:
            pass

    def buttons_placement_field(self):
        backgr = 'green'
        filling = 'both'
        exp = True
        def f(x_, y_, width_, height_):  # 
            field = tk.Frame(self, background=backgr)
            field.pack(expand=exp, fill=filling)
            field.place(x=x_,y=y_, width=width_, height=height_)
            return field
        return f
    
    def buttons(self, mstr=None):
        backgr = 'dark green'
        exp=False
        filling ='none'
        side_= 'left'
        def f(x_:int, y_:int, width_:int, txt:str, comm):
            if mstr == None:
                button = tk.Button(
                    master=self, text=txt, command=comm, background=backgr)
            else:
                button = tk.Button(
                    master=mstr, text=txt, command=comm, background=backgr)
            button.pack(expand=exp, fill=filling, side=side_)
            button.place(x=x_, y=y_, width=width_)
            return button
        return f
    
    def fake(self):
        pass

    def image_path(self):
        OpenImageSelector(self.image_open)
        # OpenPathImage(self.image_open)
    
    def image_open(self, file_path):

        '''
        find all paths to images on hard drive,
        add them to selection window,
        select image to display,
        push button to display image
        '''
        # ftypes = [('Python files', '*.py'), ('All files', '*')]
        # p = 'd:\\frankenstein_s escape\\effects\\PTModelSprite_ID106841.png'
        # self.image.open(file_path)
        # print(file_path)
        self.image = ImageTk.PhotoImage(Image.open(file_path))
        self.display_image(self.image)
    
    def url_link(self):
        OpenUrlImage(self.image_open_url)
    
    def image_open_url(self, link):
        # link = 'https://img2.joyreactor.com/pics/post/funny-pictures-dog-fluffy-6466914.jpeg'
        conn = urllib.request.urlopen(link)
        self.image = ImageTk.PhotoImage(Image.open(conn))
        self.display_image(self.image)

        
        # return image_field
        
        # p = []
        # im_name = 'PTModelSprite_ID106841.png'
        # directories = ['c:\\', 'd:\\']
        # for directory in directories:
        #     for r, d, files in os.walk(directory):
        #         for f in files:
        #             if f == im_name:
        #                 print(os.path.join(r, f))
        #                 # p.append(os.path.join(r, f))
        #                 break

        # img.show()
        
    
    def display_image(self, img):
        image_field = tk.Label(self)  # , background='red'
        image_field.pack(expand=True, fill='both')
        image_field.place(x=30, y=65, width=1010, height=700)
        # disp_img = ImageTk.PhotoImage(img)
        image_field.configure(image=img)
        image_field.image = img

        # # image = ImageTk.PhotoImage(Image.open(p))  # , text='image'
        # # image_field = tk.Frame(root, image_field=image)
        # # image_field.pack(expand=True, fill='both')
        # # image_field.place(relx=0.217, rely=0.1)


    
    def widgets(self):
        # buttons place
        self.button_field = self.buttons_placement_field()

        # top buttons place
        top_button_field = self.button_field(
            x_=30, y_=19, width_=1010, height_=40)

        # top buttons
        top_buttons = self.buttons(mstr=top_button_field)
        top_buttons(x_=10, y_=6, width_=100, txt='File', 
                    comm=lambda: [
                        self.file_buttons(), 
                        self.edit_button_field.destroy()\
                            if hasattr(self, 'edit_button_field')\
                                else self.fake(),
                        self.color_button_field.destroy()\
                            if hasattr(self, 'color_button_field')\
                                else self.fake(),
                        self.filter_button_field.destroy()\
                            if hasattr(self, 'filter_button_field')\
                                else self.fake()
                        ])  # file = 
        top_buttons(x_=120, y_=6, width_=100, txt='Edit', 
                    comm=lambda: [
                        self.edit_buttons(),
                        self.file_button_field.destroy()\
                            if hasattr(self, 'file_button_field')\
                                else self.fake(),
                        self.color_button_field.destroy()\
                            if hasattr(self, 'color_button_field')\
                                else self.fake(),
                        self.filter_button_field.destroy()\
                            if hasattr(self, 'filter_button_field')\
                                else self.fake()
                        ])  # edit = 
        top_buttons(x_=230, y_=6, width_=100, txt='Colors', 
                    comm=lambda:[
                        self.color_buttons(),
                        self.file_button_field.destroy()\
                            if hasattr(self, 'file_button_field')\
                                else self.fake(),
                        self.edit_button_field.destroy()\
                            if hasattr(self, 'edit_button_field')\
                                else self.fake(),
                        self.filter_button_field.destroy()\
                            if hasattr(self, 'filter_button_field')\
                                else self.fake()
                        ])  # colors = 
        top_buttons(x_=340, y_=6, width_=100, txt='Filters', 
                    comm=lambda:[
                        self.filter_buttons(),
                        self.file_button_field.destroy()\
                            if hasattr(self, 'file_button_field')\
                                else self.fake(),
                        self.edit_button_field.destroy()\
                            if hasattr(self, 'edit_button_field')\
                                else self.fake(),
                        self.color_button_field.destroy()\
                            if hasattr(self, 'color_button_field')\
                                else self.fake()
                        ])  # filters = 
    
    def file_buttons(self):
        # file buttons place
        self.file_button_field = self.button_field(
            x_=40, y_=60, width_=100, height_=135
            )
        
        # file buttons
        f_buttons = self.buttons(self.file_button_field)
        f_buttons(
            x_=6, y_=10, width_=85, txt='Open file', 
            comm=lambda: [self.image_path(), self.file_button_field.destroy()])  # file_open = 
        f_buttons(
            x_=6, y_=40, width_=85,txt='Open url', 
            comm=lambda: [self.url_link(), self.file_button_field.destroy()])  # file_open_url = 
        f_buttons(
            x_=6, y_=70, width_=85, txt='Save', 
            comm=lambda: [self.fake(), self.file_button_field.destroy()])  # file_save = 
        f_buttons(
            x_=6, y_=100, width_=85, txt='Save as', 
            comm=lambda: [self.save_image_as(), self.file_button_field.destroy()])  # file_save_as = 

    def edit_buttons(self):
        # edit buttons place
        self.edit_button_field = self.button_field(
            x_=150, y_=60, width_=100, height_=135)

        # edit buttons
        e_buttons = self.buttons(mstr=self.edit_button_field)
        e_buttons(
            x_=6, y_=10, width_=85, txt='Crop image', 
            comm=lambda: [self.fake(), self.edit_button_field.destroy()])  # edit_crop = 
        e_buttons(
            x_=6, y_=40, width_=85, txt='Flip image', 
            comm=lambda: [self.fake(), self.edit_button_field.destroy()])  # edit_flip = 
        e_buttons(
            x_=6, y_=70, width_=85, txt='Rotate', 
            comm=lambda: [self.fake(), self.edit_button_field.destroy()])  # edit_rotate = 
        e_buttons(
            x_=6, y_=100, width_=85, txt='Resize', 
            comm=lambda: [self.fake(), self.edit_button_field.destroy()])  # edit_resize = 


    def color_buttons(self):
        # color buttons place
        self.color_button_field = self.button_field(
            x_=260, y_=60, width_=100, height_=195)

        # color buttons
        color_buttons = self.buttons(mstr=self.color_button_field)
        color_buttons(
            x_=6, y_=10, width_=85, txt='Color Balance', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_balance = 
        color_buttons(
            x_=6, y_=40, width_=85, txt='Contrast', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_contrast = 
        color_buttons(
            x_=6, y_=70, width_=85, txt='Destaturate', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_COL_to_BW = 
        color_buttons(
            x_=6, y_=100, width_=85, txt='Brightness', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_brightness = 
        color_buttons(
            x_=6, y_=130, width_=85, txt='Sharpness', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_sharpness = 
        color_buttons(
            x_=6, y_=160, width_=85, txt='Color Noise', 
            comm=lambda: [self.fake(), self.color_button_field.destroy()])  # color_noise = 

    def filter_buttons(self):
        # filter buttons place
        self.filter_button_field = self.button_field(
            x_=370, y_=60, width_=100, height_=195)

        # filter buttons
        filter_buttons = self.buttons(mstr=self.filter_button_field)
        filter_buttons(
            x_=6, y_=10, width_=85, txt='Blur', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_blur = 
        filter_buttons(
            x_=6, y_=40, width_=85, txt='Contour', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_contour = 
        filter_buttons(
            x_=6, y_=70, width_=85, txt='Edge Enhance', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_edge_enhance = 
        filter_buttons(
            x_=6, y_=100, width_=85, txt='Emboss', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_emboss = 
        filter_buttons(
            x_=6, y_=130, width_=85, txt='Unsharp', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_unsharp = 
        filter_buttons(
            x_=6, y_=160, width_=85, txt='Smooth', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_smooth = 
    
    def save_image_as(self):
        file_save = filedialog.asksaveasfile(defaultextension='.jpg')
        self.image.save(file_save)
        # SaveAs(self.save_name)
    
    # def save_name(self, name):
    #     fpath = os.getcwd()
    #     fullpath = os.path.join(fpath, name+'.jpg')
    #     if len(name):
    #         if name.endswith('.jpg'):
    #             fname = name
    #         else:
    #             fname = name + '.jpg'
    #     else:
    #         fjpeg = self.find_jpeg(fpath)
    #         if len(fjpeg):
    #             dig = int([
    #                 x for x in fjpeg[-1].split('.')[0] if x.isdigit() ][0])
    #             fname = f'image{dig+1}.jpg'
    #         else:
    #             fname = 'image1.jpg'
    #     print(fname)


            


        # print(fullpath)
    
    # def find_jpeg(self, fp):
    #     fjp = []
    #     for r, d, files in os.walk(fp):
    #         for f in files:
    #             if f.endswith('.jpg'):
    #                 fjp.append(f)
    #     return fjp

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
            f.write(path_folder + '\n')
        OpenPathImage(self.update_a, path_folder)
    
    def submit_drive(self):
        path_drive = self.drives_field.get()
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_drive + '\n')
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
        imgs_path = r'D:\frankenstein_s escape\images'
        if '\\' in self.update_b:
            self.im_files = self.find_images([self.update_b])  # avaible_hard_drives ['C:\\']['D:\\']
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
        with open('recent_comp_paths.txt', 'w') as f:
            f.write(path_a + '\n')
        self.update_a(path_a)


class OpenUrlImage:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Open image from url')
        top.geometry('400x300')
        self.update = update

        # uframe = tk.Frame(top)  # , background='brown'
        # uframe.pack(expand=True, fill='both')
        # uframe.place(relx=0.03, rely=0.1, relwidth=0.92, relheight=0.85)

        ulabel = tk.Label(top, text='Insert link url:')  # , font=('arial', 12)
        ulabel.pack()
        ulabel.place(x=10, y=5)  # , width=370, height=0.3

        self.textfield = tk.Entry(top)  # , font=('arial', 12)
        self.textfield.pack(expand=True, fill='x')
        self.textfield.place(x=10, y=26, width=350, height=25)  # 
        self.textfield.focus()

        button = tk.Button(
            top, text='Open link',
            command=lambda: [self.submit(), top.destroy()]
        )
        button.pack()
        button.place(x=10, y=60, width=100, height=30)

        recent_label = tk.Label(top, text='Recent url links:')
        recent_label.pack()
        recent_label.place(x=10, y=110)

        self.recent_field = tk.Listbox(top)
        self.recent_field.pack()
        self.recent_field.place(x=10, y=130, width=350, height=120)

        self.recent_ls = []
        with open('recent_url_paths.txt', 'r') as f:
            for file in f.readlines():
                self.recent_field.insert(tk.END, file[:-1])
                self.recent_ls.insert(0, file[:-1])

        recent_button = tk.Button(
            top,
            text='Open selected link',
            command=lambda:[self.submit_recent(), top.destroy()])
        recent_button.pack()
        recent_button.place(x=10, y=260)

    def submit(self):
        '''
        !! overwrites txt file -> first line !!
        '''
        path_a = self.textfield.get()
        with open('recent_url_paths.txt', 'w') as f:
            f.write(path_a + '\n')
        self.update(path_a)
    
    def submit_recent(self):
        recent_url = self.recent_field.curselection()[0]
        print(self.recent_ls[recent_url])
        self.update(self.recent_ls[recent_url])

# class SaveAs:
#     def __init__(self, update):
#         top = tk.Toplevel()
#         top.title('Save as')
#         top.geometry('400x200')
#         self.update = update
        
#         sframe = tk.Frame(top)  # , background='brown'
#         sframe.pack(expand=True, fill='both')
#         sframe.place(relx=0.03, rely=0.1, relwidth=0.92, relheight=0.85)

#         slabel_txt = '''If textfield will be empty saved file
#         will be named: "image1, image2, ..."'''
#         slabel = tk.Label(sframe, text=slabel_txt, font=('arial', 12))
#         slabel.pack()
#         slabel.place(relx=0.03, rely=0.1, relwidth=0.9, relheight=0.3)

#         self.textfield = tk.Entry(
#             sframe, font=('arial', 12)
#         )
#         self.textfield.pack(expand=True, fill='x')
#         self.textfield.place(
#             relx=0.03, rely=0.56, relwidth=0.8, relheight=0.2
#             )
#         self.textfield.focus()

#         button = tk.Button(
#             sframe, text='Save file',
#             command=lambda: [self.submit(), top.destroy()]
#         )
#         button.pack()
#         button.place(relx=0.25, rely=0.85, relwidth=0.55, relheight=0.15)


#     def submit(self):
#         self.update(self.textfield.get())
    


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

# root = tk.Tk()
# root.title('Image Editor')
# root.geometry('1080x810')
# root.resizable(False, False)
# p = []

# def buttons_placement_field(main):
#     backgr = 'green'
#     filling = 'both'
#     exp = True
#     def f(x_, y_, width_, height_):  # 
#         field = tk.Frame(master=main, background=backgr)
#         field.pack(expand=exp, fill=filling)
#         field.place(x=x_,y=y_, width=width_, height=height_)
#         return field
#     return f

# def buttons(main):
#     backgr = 'dark green'
#     exp=False
#     filling ='none'
#     side_= 'left'
#     def f(x_:int, y_:int, width_:int, txt:str, comm):
#         button = tk.Button(master=main, text=txt, command=comm, background=backgr)
#         button.pack(expand=exp, fill=filling, side=side_)
#         button.place(x=x_, y=y_, width=width_)
#         return button
#     return f

# def fake():
#     pass

# def image_open():
#     p = []
#     im_name = 'PTModelSprite_ID106841.png'
#     directories = ['c:\\', 'd:\\']
#     for directory in directories:
#         for r, d, files in os.walk(directory):
#             for f in files:
#                 if f == im_name:
#                     p.append(os.path.join(r, f))
#                     break
#     root.focus()

# def file_buttons():
#     # file buttons place
#     file_button_field = button_field(x_=40, y_=60, width_=100, height_=135)
    
#     # file buttons
#     f_buttons = buttons(file_button_field)
#     f_buttons(
#         x_=6, y_=10, width_=85, txt='Open file', 
#         comm=lambda: [image_open(), file_button_field.destroy()])  # file_open = 
#     f_buttons(
#         x_=6, y_=40, width_=85,txt='Open url', 
#         comm=lambda: [fake(), file_button_field.destroy()])  # file_open_url = 
#     f_buttons(
#         x_=6, y_=70, width_=85, txt='Save', 
#         comm=lambda: [fake(), file_button_field.destroy()])  # file_save = 
#     f_buttons(
#         x_=6, y_=100, width_=85, txt='Save as', 
#         comm=lambda: [fake(), file_button_field.destroy()])  # file_save_as = 

# def edit_buttons():
#     # edit buttons place
#     edit_button_field = button_field(x_=150, y_=60, width_=100, height_=135)

#     # edit buttons
#     e_buttons = buttons(edit_button_field)
#     e_buttons(
#         x_=6, y_=10, width_=85, txt='Crop image', 
#         comm=lambda: [fake(), edit_button_field.destroy()])  # edit_crop = 
#     e_buttons(
#         x_=6, y_=40, width_=85, txt='Flip image', 
#         comm=lambda: [fake(), edit_button_field.destroy()])  # edit_flip = 
#     e_buttons(
#         x_=6, y_=70, width_=85, txt='Rotate', 
#         comm=lambda: [fake(), edit_button_field.destroy()])  # edit_rotate = 
#     e_buttons(
#         x_=6, y_=100, width_=85, txt='Resize', 
#         comm=lambda: [fake(), edit_button_field.destroy()])  # edit_resize = 


# def color_buttons():
#     # color buttons place
#     color_button_field = button_field(x_=260, y_=60, width_=100, height_=195)

#     # color buttons
#     color_buttons = buttons(color_button_field)
#     color_buttons(
#         x_=6, y_=10, width_=85, txt='Color Balance', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_balance = 
#     color_buttons(
#         x_=6, y_=40, width_=85, txt='Contrast', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_contrast = 
#     color_buttons(
#         x_=6, y_=70, width_=85, txt='Destaturate', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_COL_to_BW = 
#     color_buttons(
#         x_=6, y_=100, width_=85, txt='Brightness', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_brightness = 
#     color_buttons(
#         x_=6, y_=130, width_=85, txt='Sharpness', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_sharpness = 
#     color_buttons(
#         x_=6, y_=160, width_=85, txt='Color Noise', 
#         comm=lambda: [fake(), color_button_field.destroy()])  # color_noise = 

# def filter_buttons():
#     # filter buttons place
#     filter_button_field = button_field(x_=370, y_=60, width_=100, height_=195)

#     # filter buttons
#     filter_buttons = buttons(filter_button_field)
#     filter_buttons(
#         x_=6, y_=10, width_=85, txt='Blur', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_blur = 
#     filter_buttons(
#         x_=6, y_=40, width_=85, txt='Contour', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_contour = 
#     filter_buttons(
#         x_=6, y_=70, width_=85, txt='Edge Enhance', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_edge_enhance = 
#     filter_buttons(
#         x_=6, y_=100, width_=85, txt='Emboss', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_emboss = 
#     filter_buttons(
#         x_=6, y_=130, width_=85, txt='Unsharp', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_unsharp = 
#     filter_buttons(
#         x_=6, y_=160, width_=85, txt='Smooth', 
#         comm=lambda: [fake(), filter_button_field.destroy()])  # filter_smooth = 

# # buttons place
# button_field = buttons_placement_field(root)

# # top buttons place
# top_button_field = button_field(x_=30, y_=19, width_=1010, height_=40)

# # top buttons
# top_buttons = buttons(top_button_field)
# file = top_buttons(x_=10, y_=6, width_=100, txt='File', comm=lambda: [file_buttons()])
# edit = top_buttons(x_=120, y_=6, width_=100, txt='Edit', comm=edit_buttons)
# colors = top_buttons(x_=230, y_=6, width_=100, txt='Colors', comm=color_buttons)
# filters = top_buttons(x_=340, y_=6, width_=100, txt='Filters', comm=filter_buttons)

# # image
# # with Image.open(p) as img:

# # image = ImageTk.PhotoImage(Image.open(p))  # , text='image'
# # image_field = tk.Frame(root, image_field=image)
# # image_field.pack(expand=True, fill='both')
# # image_field.place(relx=0.217, rely=0.1)

# # # sliders
# # sliders_field = tk.Frame(root, background='yellow')  # , text='sliders'
# # sliders_field.pack(expand=True, fill='both')
# # sliders_field.place(relx=0.217, rely=0.72, relwidth=0.75, relheight=0.25)

# root.mainloop()