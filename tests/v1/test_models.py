import pytest
from src.v1_color_explorer.models import Color, rgb_to_color

def test_rgb_to_color():
    """Convert rgb color tuple from color_extractor to color object (hex and hsl)"""

    #Create a pure red rgb
    rgb = (255, 0, 0)
    color = rgb_to_color(rgb, percentage=0.5)

    assert color.rgb == (255, 0, 0)
    assert color.hex.lower() == "#ff0000" #On the color wheel red has a hue of 0.0 degrees
    assert color.hsl[0] == pytest.approx(0.0)
    assert color.percentage == 0.5
    
    