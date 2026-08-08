"""
test_region_selector.py
Tests region_selector module

"""
import numpy as np
import pytest
import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src", "v1_color_explorer"))
from region_selector import RegionSelector

#Tests case for if the user cancels
def test_select_region_raises_cancelled():
    fake_image = np.zeros((100, 100, 3), dtype=np.uint8)
    with patch("region_selector.cv2.selectROI", return_value=(0, 0, 0, 0)):
        selector = RegionSelector(fake_image)
        with pytest.raises(ValueError):
            selector.select_region()

        
