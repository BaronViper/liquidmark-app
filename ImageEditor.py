from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageEditor:
    def editorsetup(self, window, img):
        for child in window.winfo_children():
            child.destroy()

        preview = Frame(window, height=525, width=486)
        editor = Frame(window, bg="black", height=525, width=324)
        preview.grid(row=0, column=0, sticky="nsew")
        editor.grid(row=0, column=1, sticky="nsew")

        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_rowconfigure(0, weight=1)

        panel = Label(preview, image=img)

        # set the image as img
        panel.image = img
        panel.place(x=243, y=262.5, anchor='center')

        # Editor panel setup
        watermark_text = Label(editor, text="Upload Watermark", bg='black', fg='white')
        watermark_text.grid(row=0, column=1)
