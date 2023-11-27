import tkinter as tk

from utils import Utils


class SaveAs(Utils):
    def __init__(self, update):
        top = tk.Toplevel(
            background=self.app_colors()['color_butt_place_field'])
        top.title('Save as')
        top.geometry('400x250')
        self.update = update
        
        label = self.labels(top)
        label('File name (default:"image_"):', 10, 25)
        label('Image format (default: original format): jpg, png, tiff', 10, 80)  # 75
        label('Path to save the image (default: Documents path)', 10, 135)  # 125

        field = self.entries(top)
        field(10, 45, 300, 25)
        field(10, 100, 50, 25)  # 95
        field(10, 155, 300, 25)  # 145

        button = self.buttons(top)
        button('Save as', top.destroy, x_=80, y_=200, width_=100, height_=25)
        button('Cancel', top.destroy, x_=200, y_=200, width_=100, height_=25)

            
        
        # sframe = tk.Frame(top)  # , background='brown'
        # sframe.pack(expand=True, fill='both')
        # sframe.place(relx=0.03, rely=0.1, relwidth=0.92, relheight=0.85)

        # slabel_txt = '''If textfield will be empty saved file
        # will be named: "image1, image2, ..."'''
        # slabel = tk.Label(sframe, text=slabel_txt)
        # slabel.pack()
        # slabel.place(relx=0.03, rely=0.1, relwidth=0.9, relheight=0.3)

        # self.textfield = tk.Entry(
        #     sframe, font=('arial', 12)
        # )
        # self.textfield.pack(expand=True, fill='x')
        # self.textfield.place(
        #     relx=0.03, rely=0.56, relwidth=0.8, relheight=0.2
        #     )
        # self.textfield.focus()

        # button = tk.Button(
        #     sframe, text='Save file',
        #     command=lambda: [self.submit(), top.destroy()]
        # )
        # button.pack()
        # button.place(relx=0.25, rely=0.85, relwidth=0.55, relheight=0.15)


    def submit(self):
        self.update(self.textfield.get())