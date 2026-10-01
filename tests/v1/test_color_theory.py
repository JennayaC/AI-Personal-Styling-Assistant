import pytest
from src.v1_color_explorer.color_theory import hue_distance
from src.v1_color_explorer.color_theory import is_monochromatic
from src.v1_color_explorer.color_theory import is_analogous
from src.v1_color_explorer.color_theory import is_complementary
from src.v1_color_explorer.color_theory import is_triadic
from src.v1_color_explorer.models import Color

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


def make_color(hue:float) -> Color:
    """Helper function for making a color to avoid repetitive code"""
    return Color(hex="#000000", rgb=(0,0,0), hsl=(hue, 0.5, 0.5), percentage=0.2)

def test_monochromatic_true():
    """Test that monochromatic colors are correctly identified"""
    colors =[make_color(210.0), make_color(215.0), make_color(220.0)]
    assert is_monochromatic(colors) is True

def test_monochromatic_false():
    """Test that non-monochromatic colors are correctly identified"""
    colors =[make_color(210.0), make_color(230.0), make_color(250.0)]
    assert is_monochromatic(colors) is False

def test_monochromatic_wrap_around():
    """Test that monochromatic colors are correctly identified with wrap around"""
    colors =[make_color(5.0), make_color(355.0)]
    assert is_monochromatic(colors) is True

def test_analogous_true():
    """Test that analogous colors are correctly identified"""
    colors = [make_color(10.0), make_color(50.0), make_color(35.0)]
    assert is_analogous(colors) is True

def test_analogous_false():
    """Test that non-analogous colors are correctly identified"""
    colors = [make_color(10.0), make_color(90.0), make_color(200.0)]
    assert is_analogous(colors) is False

def test_analogous_wrap_around():
    """Test that analogous colors are correctly identified with wrap around"""
    colors = [make_color(350.0), make_color(10.0), make_color(20.0)]
    assert is_analogous(colors) is True

def test_complementary_true():
    """Test that complementary colors are correctly identified"""
    colors = [make_color(180.0), make_color(0.0)]
    assert is_complementary(colors) is True

def test_complementary_false():
    """Test that non-complementary colors are correctly identified"""
    colors = [make_color(180.0), make_color(90.0)]
    assert is_complementary(colors) is False

def test_complementary_wrap_around():
    """Test that complementary colors are correctly identified with wrap around"""
    colors = [make_color(350.0), make_color(170.0)]
    assert is_complementary(colors) is True

def test_triadic_true():
    """Test that triadic colors are correctly identified"""
    colors = [make_color(180.0), make_color(300.0), make_color(60.0)]
    assert is_triadic(colors) is True

def test_triadic_false():
    """Test that non-triadic colors are correctly identified"""
    colors = [make_color(180.0), make_color(0.0), make_color(200.0)]
    assert is_triadic(colors) is False

def test_triadic_wrap_around():
    """Test that triadic colors are correctly identified with wrap around"""
    colors = [make_color(305.0), make_color(65.0), make_color(185.0)]
    assert is_triadic(colors) is True

def test_triadic_false_two_identical_colors():
    """Test that non-triadic colors are correctly identified"""
    colors = [make_color(180.0), make_color(300.0), make_color(300.0)]
    assert is_triadic(colors) is False
