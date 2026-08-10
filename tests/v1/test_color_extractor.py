import numpy as np 
import pytest
from src.v1_color_explorer.color_extractor import extract_colors

#Test to make sure the color extractor returns the correct number of colors
def test_color_extractor_returns_correct_number_of_colors():
    fake_region = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)

    result = extract_colors(fake_region, n_colors=5)

    assert len(result) == 5

#Test to ensure the colors returned are valid
def test_color_extractor_returns_valid_rgb_tuples():
    fake_region = np.random.randint(0,256, (10,10,3), dtype=np.uint8)
    
    result = extract_colors(fake_region, n_colors = 3)

    for color in result:
        assert isinstance(color, tuple), "Each color should be a tuple."
        assert len(color) == 3, "Each color tuple should have 3 values (R,G,B)."
        assert all (0 <= val <= 255 for val in color), "All values must be between 0 and 255"

#Test if an empty array is passed
def test_color_extractor_raises_value_error_for_empty_input():
    empty_region = np.zeros((0, 0, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        extract_colors(empty_region, n_colors = 5)

