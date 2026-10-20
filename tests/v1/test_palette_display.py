import pytest
import matplotlib
matplotlib.use("Agg") #This way no GUI window pops up when testing.
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from src.v1_color_explorer.models import Color, ColorRelationship
from src.v1_color_explorer.palette_display import create_figure, show_palette
from unittest.mock import patch

def make_test_color(hex_code: str, r: int, g: int, b: int, percentage: float) -> Color:
    """Helper to create color instance for testing."""
    return Color(hex=hex_code, rgb = (r, g, b), hsl = (0.0, 0.0, 0.0), percentage=percentage)


def test_create_figure_returns_figure_with_correct_swatch_count():
    """Verify create_figure produces a matplotlib Figure with one rectangle swatch per color."""
    colors = [
        make_test_color("#FF0000", 255, 0, 0, 0.5),
        make_test_color("#00FF00", 0, 255, 0, 0.3),
        make_test_color("#0000FF", 0, 0, 255, 0.2),
    ]
    relationship = ColorRelationship(
        label="triadic",
        description="The colors form a balanced triadic harmony."
    )
    fig = create_figure(colors, relationship)
    assert isinstance(fig, plt.Figure)
    
    # Check that the main axis contains 3 rectangle patches (one per color)
    ax = fig.axes[0]
    rectangles = [patch for patch in ax.patches if isinstance(patch, Rectangle)]
    assert len(rectangles) == len(colors)
    
    plt.close(fig)

def test_empty_color_list():
    """Avoid figure creation if color list is empty"""
    colors = []
    relationship = ColorRelationship(
        label="unknown",
        description="Unknown color relationship."
    )
    with pytest.raises(ValueError, match="Color list cannot be empty"):
        create_figure([], relationship)

def test_show_palette():
    """Ensure that show() displays a figure without crashing."""    
    colors = [
        make_test_color("#FF0000", 255, 0, 0, 0.5),
        make_test_color("#00FF00", 0, 255, 0, 0.3),
        make_test_color("#0000FF", 0, 0, 255, 0.2),
    ]
    relationship = ColorRelationship(
        label="triadic",
        description="The colors form a balanced triadic harmony."
    )
    with patch("src.v1_color_explorer.palette_display.plt.show") as mock_plt_show:
        show_palette(colors, relationship)
        mock_plt_show.assert_called_once()