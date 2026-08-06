"""
test_image_loader.py
Tests for the image_loader module.
"""
import pytest
import os 
import sys

# Adds the src directory to the Python path to allow importing image_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src", "v1_color_explorer"))
from image_loader import load, ImageLoadError

#Tests load function if path does not exist
def test_load_raises_for_invalid_path():
    with pytest.raises(ImageLoadError):
        load("/this/path/does/not/exist.jpg")
    
def test_load_raises_for_unsupported_format(tmp_path):
    #Creates a real file with an unsupported extension with tmp_path
    fake_gif = tmp_path / "outfit.gif"
    fake_gif.write_bytes(b"fake content")

    with pytest.raises(ImageLoadError):
        load(str(fake_gif))

def test_load_returns_ndarray_for_valid_image(tmp_path):
    import cv2
    import numpy as np 

    #Create a real 10x10 black image and save it [0, 0, 0] = black)
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    img_path = tmp_path / "outfit.jpg"
    cv2.imwrite(str(img_path), img)

    result = load(str(img_path))

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert result.shape == (10, 10, 3)

