"""
image_loader.py
Handles loading and validating image files
"""
import os
import cv2

class ImageLoadError(Exception):
    pass

SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".bmp"}

def load(file_path: str):
    """
    Validates and loads an image from the given file path. 
    Returns the image as a NumPy RGB array
    Raises ImageLoadError if the path, format, or file content is invalid.
    
    """
    #Checks if file path exists
    if not os.path.isfile(file_path):
        raise ImageLoadError(f"File not found: '{file_path}'. Please check the path and try again.")

    #Validates file format
    _, extension = os.path.splitext(file_path) #Splits file path to get extension
    if extension.lower() not in SUPPORTED_FORMATS:
        raise ImageLoadError(f"Unsupported file format: '{extension}'. Supported formats are: {SUPPORTED_FORMATS}")

    image = cv2.imread(file_path)
    if image is None:
        raise ImageLoadError(f"Could not read image at '{file_path}'. The file may be corrupted or unreadable.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Flips color values back to standard
    return image

    

