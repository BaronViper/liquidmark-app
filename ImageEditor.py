import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class ImageEditor:
    def __init__(self):
        self.target_pic_filename = None

    def select_img(self):
        filetypes = (
            ('JPEG', '*.jpeg'),
            ('PNG', '*.png'),
            ('JPG', '*.jpg')
        )
        filename = fd.askopenfilename(
            title='Upload an Image',
            initialdir='/',
            filetypes=filetypes
        )
        self.target_pic_filename = filename
