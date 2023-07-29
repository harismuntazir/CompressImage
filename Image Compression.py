# imgcom.py
import os
from PIL import Image

def compress_image(image_path, quality, max_size):
    image = Image.open(image_path).convert("RGB")
    output_path = "out_" + image_path
    
    while image.size[0] > 1:
        image.thumbnail((image.size[0]*0.9, image.size[1]*0.9))
        image.save(output_path, "JPEG", quality=quality)
        
        if os.stat(output_path).st_size / 1024 <= max_size:
            break

    return output_path

def main():
    file_name = input("Enter the image file name: ")
    compress_upto = int(input("Enter the compression quality (1-100): "))
    max_size = float(input("Enter the desired maximum size in KB: "))
    output_file = compress_image(file_name, compress_upto, max_size)

    size = os.stat(output_file).st_size / 1024
    print(f"The output file size is: {size} KB")
    print("The compression completed successfully.")

if __name__ == "__main__":
    main()
