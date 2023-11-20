import glob
import io
import os
import tkinter as tk
import urllib
from concurrent.futures import ThreadPoolExecutor
from tkinter import filedialog

import PIL
import requests
from PIL import Image, ImageDraw, ImageOps, ImageTk
from PIL.Image import Resampling

from color_balance import ColorBalance
from crop_image import CropImage
from flip_image import FlipImage
from open_path import OpenImageSelector
from open_url import OpenUrlImage
from resize_image import ResizeImage
from rotate_image import RotateImage

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
        self.dims_ = []
        self.resample_filters = {
            'nearest': Resampling.NEAREST,
            'box': Resampling.BOX,
            'bilinear': Resampling.BILINEAR,
            'hamming': Resampling.HAMMING,
            'bicubic': Resampling.BICUBIC,
            'lanchos': Resampling.LANCZOS
        }
        self.recent_paths_saver()
        self.widgets()

    def recent_paths_saver(self):
        file_comp = 'recent_comp_paths.txt'
        file_url = 'recent_url_paths.txt'
        if (file_comp and file_url) not in os.listdir():
            f_comp = open(file_comp, 'x')
            f_comp.close()
            f_url = open(file_url, 'x')
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
        image = (Image.open(file_path))
        self.image = self.resize_image_aspect_load(image)
        # self.tk_image = ImageTk.PhotoImage(self.image)
        self.dims_.clear()
        self.dims_.append((self.image.height, self.image.width))
        self.display_image(self.image)  # self.tk_image
    
    def url_link(self):
        OpenUrlImage(self.image_open_url)
    
    def image_open_url(self, link):
        # link = 'https://img2.joyreactor.com/pics/post/funny-pictures-dog-fluffy-6466914.jpeg'
        conn = urllib.request.urlopen(link)
        image = Image.open(conn)
        self.image = self.resize_image_aspect_load(image)
        self.dims_.clear()
        self.dims_.append((self.image.height, self.image.width))
        self.display_image(self.image)  # self.tk_image
        
    
    def display_image(self, img):
        im = ImageTk.PhotoImage(img)
        image_field = tk.Label(self)  # , background='red'
        image_field.pack(expand=True, fill='both')
        image_field.place(x=30, y=65, width=1010, height=700)
        image_field.configure(image=im)
        image_field.image = im

    # def display_dimensions(self):
    #     DimensionsImage(self.display_dims, self.image)
    
    # def display_dims(self, update):
    #     print(update)
        # image= self.image
    
    def image_crop(self):
        CropImage(self.crop_image, self.image)
    
    def crop_image(self, update):
        im_copy = self.image.copy()
        cancel, left, upper, right, lower = update
        # print(update)
        if cancel:
            self.image = im_copy
            self.display_image(self.image)
        else:
            # print(self.image.height, self.image.width)
            img = self.image.crop((left, upper, right, lower))
            self.dims_.clear()
            self.dims_.append((self.image.height, self.image.width))
            # print(img.height, img.width)
            self.display_image(img)
    
    def image_flip(self):
        FlipImage(self.flip_image)

    def flip_image(self, update):
        if update['vertical']:
            img = ImageOps.flip(self.image)
            # img = self.image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        if update['horizont']:
            img = ImageOps.mirror(self.image)
            # img = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.display_image(img)
    
    def image_rotate(self):
        RotateImage(self.rotate_image)
    
    def rotate_image(self, update):
        img = self.image.rotate(int(update))
        self.display_image(img)
    
    def image_resize(self):
        ResizeImage(self.resize_image)
    
    def resize_image(self, update):
        lns = len(update)
        res_dat = {
            2: self.image.resize(size=(update[0], update[1]))\
                if lns == 2 else self.fake(),
            3: self.image.resize(
                size=(update[0], update[1]),\
                    resample=self.resample_filters[update[2]])\
                        if lns == 3 else self.fake()
            }
        img = res_dat.get(lns)
        self.display_image(img)
    
    def resize_image_aspect_load(self, img):
        window_width = 1080
        window_height = 800
        img_width = img.size[0]
        img_height = img.size[1]
        # with preserving aspect ratio
        if window_width * img_height < window_height * img_width:
            img_width = max(1, img_width * window_height // img_height)
            img_height = max(1, img_height * window_width // img_width)
            img = img.resize((img_width, img_height), self.resample_filters['lanchos'])  # Resampling.LANCZOS
        else:
            pass
        return img
    
    def color_balance(self):
        ColorBalance(self.balance_color)
    
    def balance_color(self, update):
        print(update)

    
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
            x_=6, y_=70, width_=85, txt='Image test', 
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
            comm=lambda: [self.image_crop(), self.edit_button_field.destroy()])  # edit_crop = 
        e_buttons(
            x_=6, y_=40, width_=85, txt='Flip image', 
            comm=lambda: [self.image_flip(), self.edit_button_field.destroy()])  # edit_flip = 
        e_buttons(
            x_=6, y_=70, width_=85, txt='Rotate', 
            comm=lambda: [self.image_rotate(), self.edit_button_field.destroy()])  # edit_rotate = 
        e_buttons(
            x_=6, y_=100, width_=85, txt='Resize', 
            comm=lambda: [self.image_resize(), self.edit_button_field.destroy()])  # edit_resize = 


    def color_buttons(self):
        # color buttons place
        self.color_button_field = self.button_field(
            x_=260, y_=60, width_=100, height_=195)

        # color buttons
        color_buttons = self.buttons(mstr=self.color_button_field)
        color_buttons(
            x_=6, y_=10, width_=85, txt='Color Balance', 
            comm=lambda: [self.color_balance(), self.color_button_field.destroy()])  # color_balance = 
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