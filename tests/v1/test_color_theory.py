import pytest
from src.v1_color_explorer.color_theory import hue_distance

def test_hue_distance():
    """Tests basic hue distance between angles with a wrap around"""
    assert hue_distance(30.0, 90.0) == 60.0
    assert hue_distance(90.0, 30.0) == 60.0

def test_hue_distance_wrap_around():
    """Test circular distance across the 0/360 degree"""
    assert hue_distance(10.0, 350.0) == 20.0
    assert hue_distance(350.0, 10.0) == 20.0

def test_hue_distance_identical():
    """Test distance between identical hues is zero"""
    assert hue_distance(180.0, 180.0) == 0

