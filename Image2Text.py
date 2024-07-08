import os
from tkinter import filedialog, Tk
import easyocr
from PIL import Image
import cv2

def extract_text_from_image(image_path, reader):
    try:
        # Try reading the image with OpenCV first
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("OpenCV could not read the image")
        
        # If OpenCV succeeds, use EasyOCR
        result = reader.readtext(img)
        text = '\n'.join([item[1] for item in result])
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        
        # If OpenCV fails, try with PIL
        try:
            pil_image = Image.open(image_path)
            result = reader.readtext(pil_image)
            text = '\n'.join([item[1] for item in result])
            return text
        except Exception as e2:
            print(f"Error processing {image_path} with PIL: {e2}")
        
        return ""

def convert_images_to_text(image_dir, output_file):
    reader = easyocr.Reader(['en'])  # Initialize EasyOCR with English language
    
    with open(output_file, 'w', encoding='utf-8') as text_file:
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.heic')):
                image_path = os.path.join(image_dir, filename)
                print(f"Processing {filename}...")
                
                extracted_text = extract_text_from_image(image_path, reader)
                if extracted_text:
                    text_file.write(f"--- {filename} ---\n{extracted_text}\n\n")
                else:
                    text_file.write(f"--- {filename} ---\nNo text could be extracted\n\n")

def main():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    image_dir = filedialog.askdirectory(title="Select Image Directory")
    
    if not image_dir:
        print("No directory selected. Exiting.")
        return

    output_file = 'extracted_text.txt'
    convert_images_to_text(image_dir, output_file)
    print(f"Text extracted from images and saved to: {output_file}")

    # Open the output file for the user to see
    try:
        os.startfile(output_file)
    except AttributeError:
        import subprocess
        subprocess.call(['open', output_file])

if __name__ == "__main__":
    main()
