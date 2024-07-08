# Image2Text
Simple yet effective method of converting the text from screenshots or memes into text for AI/LLM integration

##  Image Text Extractor - Python Script

This is a Python script that extracts text from images within a selected directory. 

###  Features

* Uses EasyOCR library for optical character recognition (OCR).
* Supports various image formats (PNG, JPG, JPEG, BMP, HEIC).
* Handles potential errors during image processing with informative messages.
* Saves extracted text for each image in a separate section within an output file (`extracted_text.txt`).
* Opens the output file for the user to view the extracted text.

###  Requirements

* Python 3.x
* EasyOCR library (`pip install easyocr`)
* OpenCV library (`pip install opencv-python`)
* Pillow library (`pip install Pillow`)

###  Usage

1. Run the script (`python image_text_extractor.py`).
2. Select a directory containing your images.
3. The script will process each image, extract text, and save the results to `extracted_text.txt`.
4. The output file will be automatically opened for you to view the extracted text.

###  How it Works

1. The script uses the `tkinter` library to open a hidden file dialog window where you can select an image directory.
2. It initializes the `EasyOCR` reader for English language text extraction.
3. The script iterates through each file in the selected directory.
4. It checks if the filename extension matches supported image formats.
5. For each image, it attempts to read the image using OpenCV first. If successful, EasyOCR is used to extract text.
6. If OpenCV fails, it tries reading the image with Pillow and then uses EasyOCR.
7. Extracted text is saved to the output file along with the corresponding image filename. 
8. If no text is extracted from an image, a message indicating that is also saved to the output file.
9. Finally, the script opens the generated output file using the appropriate method for your operating system.

###  License

This script is provided for educational purposes only. You can modify and use it according to your needs but please consider adding your own license if you plan to distribute it.

