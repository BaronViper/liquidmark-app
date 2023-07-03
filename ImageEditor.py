from tkinter import *
from tkinter import filedialog as fd, colorchooser
from PIL import ImageTk, Image, ImageFont, ImageDraw
import pyglet

pyglet.font.add_file(r"assets/Blinker/Blinker-Regular.ttf")


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

        self.editor_window = Tk()
        self.editor_window.geometry("1080x540")
        self.editor_window.configure(bg="black")
        icon_image = PhotoImage(file="assets/logo-black.png")
        self.editor_window.iconphoto(False, icon_image)
        self.editor_window.title("Liquid Mark")

        self.editor_window.resizable(False, False)

        preview_panel = Frame(self.editor_window, bg="#303030", width="780", height="540", relief="sunken",
                              borderwidth=3)
        preview_panel.grid(row=0, column=0, sticky="nsew")

        self.im_label = Label(preview_panel, borderwidth=0, justify='center')

        editor_panel = Frame(self.editor_window, bg="black", width="300", height="540")
        editor_panel.grid(row=0, column=1, sticky="nsew")

        self.editor_window.columnconfigure(1, weight=1)

        self.im = Image.open(self.target_pic_filename)
        max_height = 480
        width_ratio = max_height / self.im.height
        new_width = int(self.im.width * width_ratio)
        self.resized_image = self.im.resize((new_width, max_height))

        self.color_code = ((0, 0, 0), '#000000')

        photo = ImageTk.PhotoImage(self.resized_image)

        self.im_label.image = photo  # Store a reference to the PhotoImage object
        self.im_label.configure(image=photo)
        preview_panel.pack_propagate(False)
        self.im_label.pack(expand=True)

        editor_title = Label(editor_panel, text="Liquid Mark", font=("Blinker", 15, "bold"), background='black',
                             foreground="white")
        editor_title.grid(row=0, columnspan=2, pady=10)

        editor_panel.grid_columnconfigure(0, weight=1)
        editor_panel.grid_columnconfigure(1, weight=1)

        watermark_text_label = Label(editor_panel, text="Watermark Text:", font=("Blinker", 12),
                                     background='black', foreground="white")
        watermark_text_label.grid(row=1, column=0, sticky="nsew")

        self.watermark_text = Entry(editor_panel)
        self.watermark_text.grid(row=1, column=1, sticky="w", padx=3, ipadx=15)

        orient_label_x = Label(editor_panel, text="X Position:", font=("Blinker", 12), background="black",
                               foreground="white")
        orient_label_x.grid(row=2, column=0, pady=30, sticky="nsew")

        self.x_scale = Scale(editor_panel, from_=0, to=photo.width(), orient=HORIZONTAL, background="black",
                             foreground="white", relief="flat", borderwidth=0)
        self.x_scale.grid(row=2, column=1, sticky="w", padx=3, ipadx=25)

        orient_label_y = Label(editor_panel, text="Y Position:", font=("Blinker", 12), background="black",
                               foreground="white")
        orient_label_y.grid(row=3, column=0, pady=10, sticky="nsew")

        self.y_scale = Scale(editor_panel, from_=0, to=photo.height(), orient=HORIZONTAL, background="black",
                             foreground="white", relief="flat", borderwidth=0)
        self.y_scale.grid(row=3, column=1, sticky="w", padx=3, ipadx=25)

        rotation_label = Label(editor_panel, text="Rotation:", font=("Blinker", 12), background="black",
                               foreground="white")
        rotation_label.grid(row=4, column=0, sticky="nsew", pady=30, padx=3)

        rotation_scale = Scale(editor_panel, from_=0, to=360, orient=HORIZONTAL, background="black", foreground="white",
                               relief="flat", borderwidth=0)
        rotation_scale.grid(row=4, column=1, sticky="w", ipadx=25)

        size_label = Label(editor_panel, text="Size:", font=("Blinker", 12), background="black",
                               foreground="white")
        size_label.grid(row=5, column=0, sticky="nsew", pady=30, padx=3)

        self.size_scale = Scale(editor_panel, from_=0, to=self.resized_image.width, orient=HORIZONTAL, background="black", foreground="white",
                               relief="flat", borderwidth=0)
        self.size_scale.set(24)
        self.size_scale.grid(row=5, column=1, sticky="w", ipadx=25)

        color_button = Button(editor_panel, text="Select a Color", command=self.choose_color, width=30,
                              font=("Blinker", 10, "bold"))
        color_button.grid(row=6, column=0, columnspan=2)

        opacity_label = Label(editor_panel, text="Opacity:", font=("Blinker", 12), background="black",
                              foreground="white")
        opacity_label.grid(row=7, column=0, sticky="nsew", pady=30, padx=3)

        self.opacity_scale = Scale(editor_panel, from_=0, to=255, orient=HORIZONTAL, background="black",
                                   foreground="white",
                                   relief="flat", borderwidth=0)
        self.opacity_scale.set(255)
        self.opacity_scale.grid(row=7, column=1, sticky="w", ipadx=25)

        save_button = Button(editor_panel, text="Save Image", width=30, font=("Blinker", 10, "bold"),
                             command=self.save_image)
        save_button.grid(row=8, column=0, columnspan=2)

        self.watermarking()
        self.editor_window.after(100, self.continuous_watermarking)

    def choose_color(self):
        # variable to store hexadecimal code of color
        self.color_code = colorchooser.askcolor(title="Choose color")

    def save_image(self):
        filetypes = (
            ('Custom Image', '*.jpg *.jpeg *.png'),
        )
        save_path = fd.asksaveasfilename(defaultextension='.png', filetypes=filetypes)
        output_image = ImageTk.getimage(self.watermarked_photo)

        original_proc = output_image.resize((self.im.width, self.im.height))
        original_proc.save(fp=save_path, format="png")

    def continuous_watermarking(self):
        # Call self.watermarking method
        self.watermarking()

        # Schedule self.watermarking to be called again after 100 milliseconds
        self.editor_window.after(100, self.continuous_watermarking)

    def watermarking(self):
        text = self.watermark_text.get()
        watermarked_image = self.resized_image.copy()

        draw = ImageDraw.Draw(watermarked_image)

        font_size = int(self.size_scale.get())
        font = ImageFont.truetype(r"assets/Blinker/Blinker-Regular.ttf", font_size)

        draw.text((self.x_scale.get(), self.y_scale.get()), text, font=font,
                  fill=self.color_code[0] + (self.opacity_scale.get(),))

        self.watermarked_photo = ImageTk.PhotoImage(watermarked_image)

        self.im_label.configure(image=self.watermarked_photo)
        self.im_label.image = self.watermarked_photo
