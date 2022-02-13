import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont, ImageTk

TEXT = 'Your_text'
FONT='arial.ttf'
FONT_SIZE=20

class AppWindow:
    window = tk.Tk()
    window.title('WaterMark')
    window.geometry('508x570')

    def __init__(self):
        self.canvas = tk.Canvas(height=500, width=500)
        self.canvas.grid(row=2, column=0, columnspan=4)
        self.label = tk.Label(text='')
        self.label.grid(row=1, column=0, columnspan=3)

    def create_window(self):
        button_1 = tk.Button(self.window, text='Open Image', command=self.open_file)
        button_2 = tk.Button(self.window, text='Create Watermark', command=self.create_watermark)
        button_3 = tk.Button(self.window, text='Save Image', command=self.save_watermark)
        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=2)

    def open_file(self):
        self.filename = askopenfilename()
        self.img = Image.open(self.filename)
        x = int(self.img.size[0] / (self.img.size[0] / 500))
        y = int(self.img.size[1] / (self.img.size[1] / 500))
        img_1 = self.img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img_1)
        self.label.config(text=self.filename)
        self.canvas.create_image(0, 0, image=image, anchor='nw')
        self.canvas.image = image

    def create_watermark(self):
        idraw = ImageDraw.Draw(self.img)
        font = ImageFont.truetype(FONT, FONT_SIZE)
        idraw.text((10, 25), TEXT, font=font)
        x = int(self.img.size[0] / (self.img.size[0] / 500))
        y = int(self.img.size[1] / (self.img.size[1] / 500))
        img_1 = self.img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img_1)
        self.canvas.create_image(0, 0, image=image, anchor='nw')
        self.canvas.image = image

    def save_watermark(self):
        name = self.filename.split('.')
        self.img.save(f'{name[0]}_watermark.{name[1]}')

    def start_app(self):
        self.create_window()
        self.window.mainloop()


new = AppWindow()
new.start_app()

