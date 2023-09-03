import tkinter as tk
from tkinter import filedialog
from tkinter import Scale, Entry, Button, messagebox
from PIL import Image
import os

# Global variable to store the image path
image_path = None

def compress_image(image_path, quality, max_size):
    image = Image.open(image_path).convert("RGB")
    output_path = os.path.dirname(image_path) + "/out_" + os.path.basename(image_path)
    
    while image.size[0] > 1:
        image.thumbnail((image.size[0]*0.9, image.size[1]*0.9))
        image.save(output_path, "JPEG", quality=quality)
        
        if os.stat(output_path).st_size / 1024 <= max_size:
            break

    return output_path

def open_image():
    # This function will be used to open the image file
    # Open the file dialog and get the image file path
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png')])

def compress_image_button():
    # This function will be used to compress the image
    if not image_path:
        messagebox.showerror("Error", "No image file selected.")
        return

    quality = compress_slider.get()
    max_size = float(max_size_entry.get())
    output_file = compress_image(image_path, quality, max_size)

    size = os.stat(output_file).st_size / 1024
    messagebox.showinfo("Success", f"The output file size is: {size} KB\nThe compression completed successfully.")

root = tk.Tk()
root.title("Image Compresser")

# Set the minimum window size
root.minsize(500, 200)

# Center the window
window_width = 500
window_height = 200

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set the window's position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Set the window icon
root.iconbitmap('logo.ico')

# Create and place the open image button
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create and place the compression percentage slider
compress_slider = Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, label="Compression Percentage")
compress_slider.pack()

# Create and place the max output file size input
max_size_entry = Entry(root)
max_size_entry.pack()
max_size_label = tk.Label(root, text="Max Output File Size (KBs)")
max_size_label.pack()

# Create and place the compress image button
compress_button = Button(root, text="Compress", command=compress_image_button)
compress_button.pack()

root.mainloop()
