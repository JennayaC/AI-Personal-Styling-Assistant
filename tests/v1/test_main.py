import pytest
import numpy as np
from unittest.mock import patch, MagicMock

from src.v1_color_explorer.models import ColorRelationship
from src.v1_color_explorer.main import run


def test_run_successful_flow(capsys):
    """Test that main.run() completes the full pipeline on valid inputs."""

    # 1. Create fake data for each step
    fake_img = np.zeros((100, 100, 3), dtype=np.uint8)
    fake_roi = (0, 0, 50, 50)
    fake_rgb_colors = [(255, 0, 0)]
    fake_relationship = ColorRelationship("monochromatic", "The colors are monochromatic.")

    # 2. Mock external interactions using patch
    with patch("builtins.input", return_value="outfit.jpg"), \
         patch("src.v1_color_explorer.main.load", return_value=fake_img), \
         patch("src.v1_color_explorer.main.RegionSelector") as mock_selector_cls, \
         patch("src.v1_color_explorer.main.extract_colors", return_value=fake_rgb_colors), \
         patch("src.v1_color_explorer.main.analyze", return_value=fake_relationship):

        # Configure the RegionSelector mock instance
        mock_instance = MagicMock()
        mock_instance.select_region.return_value = fake_roi
        mock_selector_cls.return_value = mock_instance

        # 3. Call the orchestrator
        run()

    # 4. Check terminal output
    captured = capsys.readouterr()
    assert "monochromatic" in captured.out.lower()
