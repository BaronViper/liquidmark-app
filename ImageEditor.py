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

        preview_panel = Frame(editor_window, bg="red", width="810", height="540")
        preview_panel.pack(side=LEFT)

        im_label = Label(preview_panel, borderwidth=0, justify='center')

        editor_panel = Frame(editor_window, bg="blue", width="540", height="540")
        editor_panel.pack(side=RIGHT)

        im = Image.open(self.target_pic_filename)
        max_height = 480
        width_ratio = max_height / im.height
        new_width = int(im.width * width_ratio)
        resized_image = im.resize((new_width, max_height))

        photo = ImageTk.PhotoImage(resized_image)

        im_label.image = photo  # Store a reference to the PhotoImage object
        im_label.configure(image=photo)
        im_label.pack(anchor=CENTER)
# TODO: Fix Image display to center of preview panel
