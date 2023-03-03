import tkinter
from tkinter import filedialog as fd
from PIL import ImageTk, Image


def select_img():
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

    return filename
