import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class ImageDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Display GUI")
        self.geometry("500x400")
        self.resizable(True, True)

        # Label to display image
        self.image_label = ttk.Label(self, text="No image selected", anchor="center")
        self.image_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Browse button
        ttk.Button(self, text="Browse Image", command=self.browse_image).pack(pady=10)

        self.image = None

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if not file_path:
            return

        # Open and resize image to fit window
        img = Image.open(file_path)
        window_width = self.image_label.winfo_width() or 480
        window_height = self.image_label.winfo_height() or 320
        img = img.resize((window_width, window_height), Image.LANCZOS)

        # Convert to PhotoImage
        self.image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.image, text="")

if __name__ == "__main__":
    app = ImageDisplayApp()
    app.mainloop()