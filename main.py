from tkinter import *
from PIL import ImageTk, Image
from ImageEditor import select_img

# Configure basic tkinter window
front_window = Tk()
front_window.geometry("600x540")
front_window.resizable(False, False)

icon_image = PhotoImage(file="assets/logo-black.png")
front_window.iconphoto(False, icon_image)
front_window.title("Liquid Mark")
front_window.configure(bg="black")

front_logo = Image.open('assets/logo-black.png')
resized_image = front_logo.resize((400, 400), Image.Resampling.LANCZOS)
test = ImageTk.PhotoImage(resized_image)

logo_label = Label(front_window, image=test, borderwidth=0, highlightthickness=0)
logo_label.pack()


button_font = ("TMS Serif", 12)
submit_button = Button(front_window, text="Select an Image", font=button_font, command=select_img)
submit_button.pack()


front_window.mainloop()
