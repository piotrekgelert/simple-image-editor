import tkinter as tk


class AppButtons:

    def buttons_placement_field(self):
        backgr = '#777777'  # 'green'
        filling = 'both'
        exp = True
        def f(x_:int, y_:int, width_:int, height_:int):  # 
            field = tk.Frame(self, background=backgr)
            field.pack(expand=exp, fill=filling)
            field.place(x=x_,y=y_, width=width_, height=height_)
            return field
        return f
    
    def buttons(self, mstr=None):
        backgr = '#555555'  # 'dark green'
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
            x_=260, y_=60, width_=100, height_=225)

        # color buttons
        color_buttons = self.buttons(mstr=self.color_button_field)
        color_buttons(
            x_=6, y_=10, width_=85, txt='Color Balance', 
            comm=lambda: [self.color_balance(), self.color_button_field.destroy()])  # color_balance = 
        color_buttons(
            x_=6, y_=40, width_=85, txt='Contrast', 
            comm=lambda: [self.contrast(), self.color_button_field.destroy()])  # color_contrast = 
        color_buttons(
            x_=6, y_=70, width_=85, txt='Brightness', 
            comm=lambda: [self.brightness(), self.color_button_field.destroy()])  # color_brightness = 
        color_buttons(
            x_=6, y_=100, width_=85, txt='Sharpness', 
            comm=lambda: [self.sharpness(), self.color_button_field.destroy()])  # color_sharpness = 
        color_buttons(
            x_=6, y_=130, width_=85, txt='Destaturate', 
            comm=lambda: [self.color_desaturate(), self.color_button_field.destroy()])  # color_COL_to_BW = 
        color_buttons(
            x_=6, y_=160, width_=85, txt='Color Noise', 
            comm=lambda: [self.noise_color(), self.color_button_field.destroy()])   # color_noise =
        color_buttons(
            x_=6, y_=190, width_=85, txt='Color Invert',
            comm=lambda:[self.color_invert(), self.color_button_field.destroy()]
        )

    def filter_buttons(self):
        # filter buttons place
        self.filter_button_field = self.button_field(
            x_=370, y_=60, width_=100, height_=195)

        # filter buttons
        filter_buttons = self.buttons(mstr=self.filter_button_field)
        filter_buttons(
            x_=6, y_=10, width_=85, txt='Blur', 
            comm=lambda: [self.filter_blur(), self.filter_button_field.destroy()])  # filter_blur = 
        filter_buttons(
            x_=6, y_=40, width_=85, txt='Contour', 
            comm=lambda: [self.filter_contour(), self.filter_button_field.destroy()])  # filter_contour = 
        filter_buttons(
            x_=6, y_=70, width_=85, txt='Edge Enhance', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_edge_enhance = 
        filter_buttons(
            x_=6, y_=100, width_=85, txt='Emboss', 
            comm=lambda: [self.filter_emboss(), self.filter_button_field.destroy()])  # filter_emboss = 
        filter_buttons(
            x_=6, y_=130, width_=85, txt='Unsharp', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_unsharp = 
        filter_buttons(
            x_=6, y_=160, width_=85, txt='Smooth', 
            comm=lambda: [self.fake(), self.filter_button_field.destroy()])  # filter_smooth = 