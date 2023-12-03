import glob
import io
import os
import tkinter as tk
import urllib
from concurrent.futures import ThreadPoolExecutor
from random import randint
from tkinter import filedialog

import requests
from PIL import Image, ImageFilter, ImageOps, ImageStat, ImageTk
from PIL.Image import Resampling

from app_buttons import AppButtons
from color_filters import ColorFiltersUpto1, ColorFiltersUpto2
from crop_image import CropImage
from flip_image import FlipImage
from open_path import OpenImageSelector
from open_url import OpenUrlImage
from resize_image import ResizeImage
from rotate_image import RotateImage
from save_as import SaveAs

'''
the gui:
BUTTONS AREA:
Image file: [open file, open url, save, save as: jpeg, png, tiff, others],
Edit image: [crop, flip, rotate, resize],
Colors: [color_balance, contrast, COL_to_BW, brightness, sharpness, noise, invert]
Filters: [blur, contour, edge_enhance, emboss, unsharp, smooth]
IMAGE AREA:
SLIDERS AREA: [save to image butt(closes slider), ]

 whole code is build into an .exe file through the "pyinstaller" library
'''


class MainApp(tk.Tk, AppButtons):
    def __init__(self):
        super().__init__()
        self.title('Simple Image Editor')
        self.geometry('1080x810')
        self.resizable(False, False)
        self.configure(background='#555555')
        self.dims_ = []
        self.resample_filters = {
            'nearest': Resampling.NEAREST,
            'box': Resampling.BOX,
            'bilinear': Resampling.BILINEAR,
            'hamming': Resampling.HAMMING,
            'bicubic': Resampling.BICUBIC,
            'lanchos': Resampling.LANCZOS
        }
        self.extension = ''
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
        self.extension = '.'+file_path.split('.')[-1]
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
        self.extension = '.'+link.split('.')[-1]
        conn = urllib.request.urlopen(link)
        image = Image.open(conn)
        self.image = self.resize_image_aspect_load(image)
        self.dims_.clear()
        self.dims_.append((self.image.height, self.image.width))
        self.display_image(self.image)  # self.tk_image

    def image_crop(self):
        CropImage(self.crop_image, self.image)
    
    def crop_image(self, update):
        im_c = self.image.copy()
        apply, cancel, left, upper, right, lower = update
        # print(update)
        if (apply and cancel) == 0:
            img = im_c.crop((left, upper, right, lower))
            self.display_image(img)
        if apply == 1:
            img = im_c.crop((left, upper, right, lower))
            self.image = img
            self.dims_.clear()
            self.dims_.append((self.image.height, self.image.width))
            self.display_image(self.image)
        if cancel == 1:
            self.dims_.clear()
            self.dims_.append((self.image.height, self.image.width))
            self.display_image(self.image)
            # print(self.image.height, self.image.width)
            
    
    def image_flip(self):
        FlipImage(self.flip_image)

    def flip_image(self, update):
        if update['vertical']:
            img = ImageOps.flip(self.image)
            # img = self.image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        if update['horizont']:
            img = ImageOps.mirror(self.image)
            # img = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.image = img
        self.display_image(self.image)
    
    def image_rotate(self):
        RotateImage(self.rotate_image)
    
    def rotate_image(self, update):
        img = self.image.copy()
        key = [k for k, v in update.items() if v != 0][0]
        im = img.rotate(update[key])
        if update['cancel'] == 0:
            self.display_image(im)
        if update['cancel'] == 1:
            self.display_image(self.image)
        if update['apply'] == 1:
            self.image = im
            self.display_image(im)
    
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
        if (img_height > img_width) and (img_height > window_height):
            new_height = window_height
            new_width = new_height * img_width // img_height
            img = img.resize(
                    (new_width, new_height), 
                    self.resample_filters['lanchos']
                    )
        
        if (img_width > img_height) and (img_width > window_width):
            new_width = window_width
            new_height = new_width * img_height // img_width
            img = img.resize(
                    (new_width, new_height), 
                    self.resample_filters['lanchos']
                    )
        else:
            pass
        return img
    
    def color_balance(self):
        lab_txt = 'Adjust image color balance. \n \
        A factor of 0.0 gives a black and white image.\n \
            A factor of 1.0 gives the original image.\n \
                A factor of 2.0 gives a color vibrant image.'

        ColorFiltersUpto2(self.balance_color, 'Color Balance', lab_txt)
    
    def balance_color(self, update):
        upd_val, upd = update
        img = self.image.copy()    
        img_cl = img.convert('L').convert('RGB')
        cl_img = Image.blend(img_cl, img, upd)
        if upd_val == 1:    
            self.display_image(cl_img)
        if upd_val == 0:
            self.image = cl_img
            self.display_image(self.image)
    
    def contrast(self):
        lab_txt = 'Adjust image contrast.\n \
               An enhancement factor of 0.0 gives a solid grey image.\n \
               A factor of 1.0 gives the original image.'
        ColorFiltersUpto2(self.color_contrast, 'Contrast', lab_txt)
        # ColorFiltersUpto1(self.color_contrast, 'Contrast', lab_txt)
    
    def color_contrast(self, update):
        upd_val, upd = update
        img = self.image.copy()
        mean_ = int(ImageStat.Stat(img.convert('L')).mean[0] + 0.5)
        img_con_ = Image.new('L', img.size, mean_).convert(img.mode)
        img_con = Image.blend(img_con_, img, upd)
        if upd_val == 1:    
            self.display_image(img_con)
        if upd_val == 0:
            self.image = img_con
            self.display_image(self.image)
    
    def brightness(self):
        lab_txt = 'Adjust image brightness.\n \
               An enhancement factor of 0.0 gives a solid black image.\n \
               A factor of 1.0 gives the original image.'
        ColorFiltersUpto1(self.color_brightness, 'Brightness', lab_txt)
    
    def color_brightness(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_br_ = Image.new(img.mode, img.size, 0)
        img_br = Image.blend(img_br_, img, upd)
        if upd_val == 1:    
            self.display_image(img_br)
        if upd_val == 0:
            self.image = img_br
            self.display_image(self.image)

    def sharpness(self):
        lab_txt = 'An enhancement factor of 0.0 gives a blurred image.\n \
            A factor of 1.0 gives the original image.\n \
                A factor of 2.0 gives a sharpened image.'
        ColorFiltersUpto2(self.color_sharpness, 'Sharpness', lab_txt)
    
    def color_sharpness(self, update):
        upd_val, upd = update
        img = self.image.copy()
        # img_sharp_ = Image.new(img.mode, img.size, 0)
        img_sharp_ = img.filter(ImageFilter.SMOOTH_MORE)
        img_sharp = Image.blend(img_sharp_, img, upd)
        if upd_val == 1:    
            self.display_image(img_sharp)
        if upd_val == 0:
            self.image = img_sharp
            self.display_image(self.image)
    
    def noise_color(self):
        lab_txt = 'Adjust image noise.(Slow)\n \
               An enhancement factor of 0.0 gives a solid noise.\n \
               A factor of 1.0 gives the original image.'
        ColorFiltersUpto1(self.color_noise, 'Color noise', lab_txt)
    
    def color_noise(self, update):
        upd_val, upd = update
        img = self.image.copy()
        
        # create new noisy image
        noise_img = Image.new(self.image.mode, self.image.size)
        width, height = noise_img.size[0], noise_img.size[1]
        multiplied_dims = round(width * height)
        for _ in range(multiplied_dims):
            noise_img.putpixel(
                (randint(0, width-1), randint(0, height-1)),
                (randint(0, 255), randint(0, 255), randint(0, 255))
            )
        img_noisy = Image.blend(noise_img, img, upd)
        if upd_val == 1:    
            self.display_image(img_noisy)
        if upd_val == 0:
            self.image = img_noisy
            self.display_image(self.image)
    
    def color_desaturate(self):
        lab_txt = 'Adjust image color balance. \n \
        An enhancement factor of 0.0 gives a black and white image.\n \
        A factor of 1.0 gives the original image'
        ColorFiltersUpto1(self.desaturate_color, 'Desaturate color', lab_txt)
    
    def desaturate_color(self, update):
        upd_val, upd = update
        img = self.image.copy()    
        img_cl = img.convert('L').convert('RGB')
        cl_img = Image.blend(img_cl, img, upd)
        if upd_val == 1:    
            self.display_image(cl_img)
        if upd_val == 0:
            self.image = cl_img
            self.display_image(self.image)
    
    def color_invert(self):
        lab_txt = 'Invert image. \n \
            An factor of 0.0 gives a totally inverts colors in the image.\n \
                A factor of 1.0 gives the original image'
        ColorFiltersUpto1(self.invert_color, 'Invert image', lab_txt)
    
    def invert_color(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_inv = ImageOps.invert(img)
        inv_img = Image.blend(img_inv, img, upd)
        if upd_val == 1:
            self.display_image(inv_img)
        if upd_val == 0:
            self.image =  inv_img
            self.display_image(self.image)
    
    def filter_blur(self):
        lab_txt = 'Adjust image blur. \n \
        An enhancement factor of 0.0 gives a totally blured image.\n \
        A factor of 1.0 gives the original image'
        ColorFiltersUpto1(self.blur_filter, 'Blur image', lab_txt)
    
    def blur_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_blur = img.filter(ImageFilter.BLUR)
        blur_img = Image.blend(img_blur, img, upd)
        if upd_val == 1:
            self.display_image(blur_img)
        if upd_val == 0:
            self.image = blur_img
            self.display_image(self.image)
    
    def filter_contour(self):
        lab_txt = 'Find contour edges in image. \n \
            An enhancement factor of 0.0 gives contour edges in image. \n \
                A factor of 1.0 gives the original image.'
        ColorFiltersUpto1(self.contour_filter, 'Edge detection', lab_txt)

    def contour_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_cont = img.filter(ImageFilter.CONTOUR)
        cont_img = Image.blend(img_cont, img, upd)
        if upd_val == 1:
            self.display_image(cont_img)
        if upd_val == 0:
            self.image = cont_img
            self.display_image(self.image)

    def filter_emboss(self):
        lab_txt = 'Apply emboss to the image. \n . \
            An enhancement factor of 0.0 gives a totally applied emboss. \n . \
                A factor of 1.0 gives original image.'
        ColorFiltersUpto1(self.emboss_filter, 'Apply emboss', lab_txt)
    
    def emboss_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_emb = img.filter(ImageFilter.EMBOSS)
        emb_img = Image.blend(img_emb, img, upd)
        if upd_val == 1:
            self.display_image(emb_img)
        if upd_val == 0:
            self.image = emb_img
            self.display_image(self.image)
    
    def filter_detail(self):
        lab_txt = 'Apply detail to the image. \n . \
            An enhancement factor of 0.0 gives a totally applied detail. \n . \
                A factor of 1.0 gives original image.'
        ColorFiltersUpto1(self.detail_filter, 'Apply Detail', lab_txt)
    
    def detail_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_det = img.filter(ImageFilter.DETAIL)
        det_img = Image.blend(img_det, img, upd)
        if upd_val == 1:
            self.display_image(det_img)
        if upd_val == 0:
            self.image = det_img
            self.display_image(self.image)

    def filter_edges(self):
        lab_txt = 'Find edges in the image. \n . \
            An enhancement factor of 0.0 gives edges black image. \n . \
                A factor of 1.0 gives original image.'
        ColorFiltersUpto1(self.edges_filter, 'Find edges', lab_txt)

    def edges_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_edg = img.filter(ImageFilter.FIND_EDGES)
        edg_img = Image.blend(img_edg, img, upd)
        if upd_val == 1:
            self.display_image(edg_img)
        if upd_val == 0:
            self.image = edg_img
            self.display_image(self.image)
    
    def filter_smooth(self):
        lab_txt = 'Smooth the image. \n . \
            An enhancement factor of 0.0 gives smoother image. \n . \
                A factor of 1.0 gives original image.'
        ColorFiltersUpto1(self.smooth_filter, 'Smooth', lab_txt)
    
    def smooth_filter(self, update):
        upd_val, upd = update
        img = self.image.copy()
        img_sm = img.filter(ImageFilter.SMOOTH)
        sm_img = Image.blend(img_sm, img, upd)
        if upd_val == 1:
            self.display_image(sm_img)
        if upd_val == 0:
            self.image = sm_img
            self.display_image(self.image)

    def save_image_as(self):
        SaveAs(self.save_name)
    
    def save_name(self, update):
        file_name = update['name'] if len(update['name']) else 'image'
        extension = ''.join(['.', update['extension']])\
            if len(update['extension']) else self.extension
        file_path = update['path'] if len(update['path'])\
            else os.path.expanduser('~\Documents')

        if update['cancel'] == '0':
            j, p = self._find_image_files(file_path, file_name)
            if extension in ('.jpg', '.jpeg'):
                self._name_file(j, extension, file_name, file_path)
            if extension == '.png':
                self._name_file(p, extension, file_name, file_path)


    def _name_file(self, ls, ext, img_n, path_):
        # print('name file: {}'.format(img_n), 'ext: {}'.format(ext))
        
        dir_lst = [x for x in ls if img_n in x]
        if len(dir_lst):
            digit = dir_lst[-1].split('.')[0][-1]
            if digit.isdigit():
                self.image.save(os.path.join(path_, f'{img_n}{int(digit)+1}{ext}'))
                # print(os.path.join(path_, f'{img_n}{int(digit)+1}{ext}'))
            else:
                self.image.save(os.path.join(path_, f'{img_n}1{ext}'))
                # print(os.path.join(path_, f'{img_n}1{ext}'))
        else:
            self.image.save(os.path.join(path_, f'{img_n}1{ext}'))
            # print(os.path.join(path_, f'{img_n}1{ext}'))
    
    def _find_image_files(self, file_path, img_n):
        jpg_files = []
        png_files = []
        for f in os.listdir(file_path):
            if f'{img_n}' in f:
                if f[-4:] in ('.jpg', '.jpeg'):
                    jpg_files.append(f)
                if f[-4:] == '.png':
                    png_files.append(f)
        return jpg_files, png_files

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()