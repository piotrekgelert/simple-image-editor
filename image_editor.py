import glob
import io
import os
import tkinter as tk
import urllib
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
        self.widgets()

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

    def image_open(self):
        p = 'd:\\frankenstein_s escape\\effects\\PTModelSprite_ID106841.png'
        self.image = ImageTk.PhotoImage(Image.open(p))
        self.display_image(self.image)
    
    def image_open_url(self):
        link = 'https://img2.joyreactor.com/pics/post/funny-pictures-dog-fluffy-6466914.jpeg'
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
            comm=lambda: [self.image_open(), self.file_button_field.destroy()])  # file_open = 
        f_buttons(
            x_=6, y_=40, width_=85,txt='Open url', 
            comm=lambda: [self.image_open_url(), self.file_button_field.destroy()])  # file_open_url = 
        f_buttons(
            x_=6, y_=70, width_=85, txt='Save', 
            comm=lambda: [self.fake(), self.file_button_field.destroy()])  # file_save = 
        f_buttons(
            x_=6, y_=100, width_=85, txt='Save as', 
            comm=lambda: [self.set_image_name(), self.file_button_field.destroy()])  # file_save_as = 

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
    
    def set_image_name(self):
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
    
    def find_jpeg(self, fp):
        fjp = []
        for r, d, files in os.walk(fp):
            for f in files:
                if f.endswith('.jpg'):
                    fjp.append(f)
        return fjp



class SaveAs:
    def __init__(self, update):
        top = tk.Toplevel()
        top.title('Save as')
        top.geometry('400x200')
        self.update = update
        
        sframe = tk.Frame(top)  # , background='brown'
        sframe.pack(expand=True, fill='both')
        sframe.place(relx=0.03, rely=0.1, relwidth=0.92, relheight=0.85)

        slabel_txt = '''If textfield will be empty saved file
        will be named: "image1, image2, ..."'''
        slabel = tk.Label(sframe, text=slabel_txt, font=('arial', 12))
        slabel.pack()
        slabel.place(relx=0.03, rely=0.1, relwidth=0.9, relheight=0.3)

        self.textfield = tk.Entry(
            sframe, font=('arial', 12)
        )
        self.textfield.pack(expand=True, fill='x')
        self.textfield.place(
            relx=0.03, rely=0.56, relwidth=0.8, relheight=0.2
            )
        self.textfield.focus()

        button = tk.Button(
            sframe, text='Save file',
            command=lambda: [self.submit(), top.destroy()]
        )
        button.pack()
        button.place(relx=0.25, rely=0.85, relwidth=0.55, relheight=0.15)


    def submit(self):
        self.update(self.textfield.get())
    


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