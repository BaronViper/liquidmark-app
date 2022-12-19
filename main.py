from tkinter import *
from PIL import Image, ImageTk
from ImageEditor import ImageEditor

window = Tk()
editor = ImageEditor()

window.title("Liquid Mark")
window.geometry("600x600")

ico = Image.open('assets/logo-white.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.configure(bg="black")

logo = Image.open('assets/logo-black.png')
resize_logo = logo.resize((350, 350))

img = ImageTk.PhotoImage(resize_logo)
label = Label(window, image=img, borderwidth=0)
label.pack()

img_label = Label(window, text="Upload Image Here", bg="black", fg="white")
img_label.pack()

file = Button(window, text='Select an Image', command=editor.editorsetup(window=window))
file.pack()


window.mainloop()
