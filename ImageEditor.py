from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class ImageEditor:
    def __init__(self, init_screen):
        self.target_pic_filename = ""
        self.init_screen = init_screen

    def select_img(self, state):
        filetypes = (
            ('Custom Image', '*.jpg *.jpeg *.png'),
        )
        filename = fd.askopenfilename(
            title='Upload an Image',
            initialdir='/',
            filetypes=filetypes
        )
        self.target_pic_filename = filename

        if state == "init" and self.target_pic_filename != "":
            self.set_editor_window()

    def set_editor_window(self):
        self.init_screen.destroy()

        editor_window = Tk()
        editor_window.geometry("1080x540")
        editor_window.configure(bg="black")



