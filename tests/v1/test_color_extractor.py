import numpy as np 
import pytest
from src.v1_color_explorer.color_extractor import extract_colors

#Test to make sure the color extractor returns the correct number of colors
def test_color_extractor_returns_correct_number_of_colors():
    fake_region = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)

    result = extract_colors(fake_region, n_colors=5)

    assert len(result) == 5

