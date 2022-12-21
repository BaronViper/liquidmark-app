from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageEditor:
    def editorsetup(self, window, img):
        for child in window.winfo_children():
            child.destroy()

        window.geometry("800x600")

        preview_panel = Label(window, image=img)
        preview_panel.grid(row=2, column=2)
        panel = Label(window, image=img)

        # set the image as img
        panel.image = img
        panel.pack()
