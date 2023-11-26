import tkinter as tk

from PIL import ImageTk

from utils import Utils


class CropImage(Utils):
    def __init__(self, update, img):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title('Crop image')
        top.geometry('400x200')
        self.update = update
        self.image = img
        self.new_dims = []

        button = self.buttons(top)
        button('Get dimensions from image', self.image_dims, 10, 10, 380, 30)
        button('Cancel', lambda: [self.submit_cancel(), top.destroy()],
               50, 50, 100, 30)
        button('Apply changes & Exit', lambda: [self.submit_exit(), top.destroy()],
               170, 50, 190, 30)

        txt = '''
                Primary mouse button selects the area,
                secondary mouse button applies the chosen area
                '''
        label = self.labels(top)
        label(txt, 10, 100)
    
    def submit_cancel(self):
        cancel = 1
        apply = 0
        new_dimensions = (apply, cancel, 0, 0, 0, 0)
        self.update(new_dimensions)

    def submit_exit(self):
        cancel = 0
        apply = 1
        self.new_dims.insert(0, cancel)
        self.new_dims.insert(0, apply)
        self.update(self.new_dims)

        # print(self.new_dims)
        # pass

    def image_dims(self):
        DimensionsImage(self.display_dims, self.image)
    
    def display_dims(self, updte):
        self.new_dims.extend(updte)
        apply = 0
        cancel = 0
        new_dimensions = (
            apply,
            cancel,
            updte[0],
            updte[1],
            updte[2],
            updte[3]
            )
        self.update(new_dimensions)
        # # return updte
        # print(updte)

class DimensionsImage:
    def __init__(self, update, img):  # image
        top = tk.Toplevel()
        top.title('Image Dimensions')
        img_width = img.size[0]
        img_height = img.size[1]
        window_width = 1080
        window_height = 800
        img_width = img.size[0]
        img_height = img.size[1]
        top.geometry(f'{img_width}x{img_height}')
        self.top_x = 0
        self.top_y = 0
        self.bot_x = 0
        self.bot_y = 0
        self.update = update

        scroll_bar_right = tk.Scrollbar(top, orient='vertical')
        scroll_bar_right.pack(side='right', fill='y')

        scroll_bar_bottom = tk.Scrollbar(top, orient='horizontal')
        scroll_bar_bottom.pack(side='bottom', fill='x')

        # if window_width * img_height < window_height * img_width:
        # # if img_height > window_height or img_width > window_width:
        #     # img_width = img_width//2
        #     img_width = max(1, img_width * window_height // img_height)
        #     # with preserving aspect ratio
        #     # img_height = img_height//2
        #     img_height = max(1, img_height * window_width // img_width)

        # else:
        #     pass
        # window_width = img_width  # 1080 * 2
        # window_height = img_height  # 800 * 2
        # top.geometry(f'{window_width}x{window_height}')
            # new_img_width = img_width
            # new_img_height = img_height
        # img = image.resize((image.size[0]//2, image.size[1]//2), Image.Resampling.LANCZOS)
        
        
        self.canvas = tk.Canvas(
            top,
            width=window_width,  # img_width
            height=window_height,  # img_height
            scrollregion=(0,0, img_width, img_height)
            )
        self.canvas.pack(expand=1, fill='both')
        
        scroll_bar_right.config(command=self.canvas.yview)
        scroll_bar_bottom.config(command=self.canvas.xview)

        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image((5, 5), image=img_tk, anchor=tk.NW)

        self.rect_id = self.canvas.create_rectangle(
            self.top_x, self.top_y,
            self.top_x, self.top_y,
            dash=(2, 2), fill='', outline='white')
        
        self.canvas.bind('<Button-1>', self.gather_coords)
        self.canvas.bind('<B1-Motion>', self.update_coords)
        self.canvas.bind('<Button-3>', lambda event: [
                                                        self.submit_coords(),
                                                        top.destroy()])

        top.mainloop()
    
    def gather_coords(self, event):
        # print(event.x, event.y)
        self.top_x = event.x
        self.top_y = event.y
    
    def update_coords(self, event):
        # print(f'updated: {event.x}, {event.y}')
        self.bot_x = event.x
        self.bot_y = event.y

        self.canvas.coords(
            self.rect_id, self.top_x, self.top_y, self.bot_x, self.bot_y)

    def submit_coords(self):
        lst_coords= [self.top_x, self.top_y, self.bot_x, self.bot_y]
        self.update(lst_coords)
        # lst_coords.append((self.top_x, self.top_y))
        # ls_bott = []
        # ls_bott.append((self.bot_x, self.bot_y))
        # lst_coords.update(ls_bott[-1])
        # if len(self.lst_coords) == 2:
        #  


# with preserving aspect ratio
        #         # if window_width * img_height < window_height * img_width:
#         # # if img_height > window_height or img_width > window_width:
#         #     # img_width = img_width//2
#         #     img_width = max(1, img_width * window_height // img_height)
#         #     # with preserving aspect ratio
#         #     # img_height = img_height//2
#         #     img_height = max(1, img_height * window_width // img_width)