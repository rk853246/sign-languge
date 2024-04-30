import tkinter as tk
from PIL import Image, ImageTk

class SignLanguageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Language Learning System")

        self.image_dict = {
            'A': 'Tutorial_Images/A.jpeg',  
            'B': 'Tutorial_Images/B.jpeg',
            'C': 'Tutorial_Images/C.jpeg',
            'D': 'Tutorial_Images/D.jpeg',
            'E': 'Tutorial_Images/E.jpeg',
            'F': 'Tutorial_Images/F.jpeg',
            'G': 'Tutorial_Images/G.jpeg',
            'H': 'Tutorial_Images/H.jpeg',
            'I': 'Tutorial_Images/I.jpeg',
            'J': 'Tutorial_Images/J.jpeg',
            'K': 'Tutorial_Images/K.jpeg',
            'L': 'Tutorial_Images/L.jpeg',
            'M': 'Tutorial_Images/M.jpeg',
            'N': 'Tutorial_Images/znz.jpeg',
            'O': 'Tutorial_Images/O.jpeg',
            'P': 'Tutorial_Images/P.jpeg',
            'Q': 'Tutorial_Images/Q.jpeg',
            'R': 'Tutorial_Images/R.jpeg',
            'S': 'Tutorial_Images/S.jpeg',
            'T': 'Tutorial_Images/T.jpeg',
            'U': 'Tutorial_Images/zuz.jpeg',
            'V': 'Tutorial_Images/V.jpeg',
            'W': 'Tutorial_Images/W.jpeg',
            'X': 'Tutorial_Images/X.jpeg',
            'Y': 'Tutorial_Images/Y.jpeg',
            'Z': 'Tutorial_Images/Z.jpeg'
        }

        self.canvas = tk.Canvas(master)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.inner_frame, anchor=tk.NW)

        self.load_images()

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def load_images(self):
        row = 0
        column = 0
        for letter, image_path in self.image_dict.items():
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.inner_frame, image=photo)
            label.image = photo
            label.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            if column == 6:  # Change this value according to the number of images you want in a row
                column = 0
                row += 1
        # Update the canvas scroll region after loading all images
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.inner_frame, width=event.width)

