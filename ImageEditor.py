from tkinter import *
from tkinter import filedialog as fd, colorchooser
from PIL import ImageTk, Image
import pyglet

pyglet.font.add_file("assets/Blinker/Blinker-Regular.ttf")


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
        icon_image = PhotoImage(file="assets/logo-black.png")
        editor_window.iconphoto(False, icon_image)
        editor_window.title("Liquid Mark")

        preview_panel = Frame(editor_window, bg="#303030", width="780", height="540", relief="sunken", borderwidth=3)
        preview_panel.grid(row=0, column=0, sticky="nsew")

        im_label = Label(preview_panel, borderwidth=0, justify='center')

        editor_panel = Frame(editor_window, bg="black", width="300", height="540")
        editor_panel.grid(row=0, column=1, sticky="nsew")

        editor_window.columnconfigure(1, weight=1)

        im = Image.open(self.target_pic_filename)
        max_height = 480
        width_ratio = max_height / im.height
        new_width = int(im.width * width_ratio)
        resized_image = im.resize((new_width, max_height))

        photo = ImageTk.PhotoImage(resized_image)

        im_label.image = photo  # Store a reference to the PhotoImage object
        im_label.configure(image=photo)
        preview_panel.pack_propagate(False)
        im_label.pack(expand=True)

        editor_title = Label(editor_panel, text="Liquid Mark", font=("Blinker", 15, "bold"), background='black',
                             foreground="white")
        editor_title.grid(row=0, columnspan=2, pady=10)

        editor_panel.grid_columnconfigure(0, weight=1)
        editor_panel.grid_columnconfigure(1, weight=1)

        watermark_text_label = Label(editor_panel, text="Watermark Text:", font=("Blinker", 12),
                                     background='black', foreground="white")
        watermark_text_label.grid(row=1, column=0, sticky="nsew")

        watermark_text = Entry(editor_panel)
        watermark_text.grid(row=1, column=1, sticky="w", padx=3, ipadx=15)

        orient_label_x = Label(editor_panel, text="X Position:", font=("Blinker", 12), background="black",
                               foreground="white")
        orient_label_x.grid(row=2, column=0, pady=30, sticky="nsew")

        x_scale = Scale(editor_panel, from_=0, to=photo.width(), orient=HORIZONTAL, background="black",
                        foreground="white", relief="flat", borderwidth=0)
        x_scale.grid(row=2, column=1, sticky="w", padx=3, ipadx=25)

        orient_label_y = Label(editor_panel, text="Y Position:", font=("Blinker", 12), background="black",
                               foreground="white")
        orient_label_y.grid(row=3, column=0, pady=10, sticky="nsew")

        y_scale = Scale(editor_panel, from_=0, to=photo.height(), orient=HORIZONTAL, background="black",
                        foreground="white", relief="flat", borderwidth=0)
        y_scale.grid(row=3, column=1, sticky="w", padx=3, ipadx=25)

        rotation_label = Label(editor_panel, text="Rotation:", font=("Blinker", 12), background="black",
                               foreground="white")
        rotation_label.grid(row=4, column=0, sticky="nsew", pady=30, padx=3)

        rotation_scale = Scale(editor_panel, from_=0, to=360, orient=HORIZONTAL, background="black", foreground="white",
                               relief="flat", borderwidth=0)
        rotation_scale.grid(row=4, column=1, sticky="w", ipadx=25)

        color_button = Button(editor_panel, text="Select a Color", command=self.choose_color, width=30,
                              font=("Blinker", 10, "bold"))
        color_button.grid(row=5, column=0, columnspan=2)

        opacity_label = Label(editor_panel, text="Opacity:", font=("Blinker", 12), background="black",
                               foreground="white")
        opacity_label.grid(row=6, column=0, sticky="nsew", pady=30, padx=3)

        opacity_scale = Scale(editor_panel, from_=0, to=100, orient=HORIZONTAL, background="black", foreground="white",
                               relief="flat", borderwidth=0)
        opacity_scale.set(100)
        opacity_scale.grid(row=6, column=1, sticky="w", ipadx=25)

        save_button = Button(editor_panel, text="Save Image")
        save_button.grid(row=8, column=0)


        # new_test = Label(editor_panel, text="JOJO")
        # new_test.pack()

    def choose_color(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title="Choose color")
        print(color_code)
