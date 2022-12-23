from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from ImageEditor import ImageEditor

window = Tk()

editor = ImageEditor()


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img.thumbnail((405, 262), Image.Resampling.LANCZOS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    editor.editorsetup(window=window, img=img)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename


window.title("Liquid Mark")
window.geometry('810x525')
window.resizable(width=False, height=False)
ico = Image.open('assets/logo-white.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.configure(bg="black")

logo = Image.open('assets/logo-black.png')
resize_logo = logo.resize((350, 350))

img = ImageTk.PhotoImage(resize_logo)
label = Label(window, image=img, borderwidth=0)
label.grid(row=0, column=0, padx=230)

font_tuple = ("Trajan Pro", 20, "bold")
font_tuple2 = ("Trajan Pro", 10)
img_label = Label(window, text="Let's Get Started", bg="black", fg="white", font=font_tuple)
img_label.grid(row=1, column=0, pady=20)

file = Button(window, text='Upload an Image', command=open_img, font=font_tuple2)
file.grid(row=2, column=0, pady=(0, 50))

window.mainloop()
