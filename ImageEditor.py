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

        font_tuple2 = ("Trajan Pro", 15)

        # Editor panel setup
        watermark_text = Label(editor, text="Choose a Watermark", bg='black', fg='white', font=font_tuple2)
        watermark_text.pack(pady=(8, 8))

        wm_button_font = ('Trajan Pro', 12)
        watermark_upload = Button(editor, text="Upload Here", font=wm_button_font)
        watermark_upload.pack(pady=(0, 8))

        size = Scale(editor, from_=0, to=100, orient=HORIZONTAL, label='Size', relief=FLAT, borderwidth=0, highlightbackground='black')
        size.pack(ipadx=20, pady=(0, 8))

        opacity = Scale(editor, from_=0, to=100, orient=HORIZONTAL, label='Opacity', relief=FLAT, borderwidth=0, highlightbackground='black')
        opacity.pack(ipadx=20)
