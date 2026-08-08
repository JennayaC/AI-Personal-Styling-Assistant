"""
region_selector.py
Handles displaying the image and letting the user select a region of interest (ROI)
Maps to: FR-04
"""
import cv2

class RegionSelector:
    """Display the image and captures a mouse drawn region made by the user"""

    #Initial this class with a loaded image
    def __init__(self, image):
        self.image = image

    def select_region(self):
        """
        Allow user to select region. Raises ValueError if selection is invalid or cancelled.
        Returns (x, y, w, h) tuple for the selected region.
        """
        roi = self._get_mouse_roi(self.image)
        x, y, w, h = roi
        if w == 0 or h == 0:
            raise ValueError("No region was selected, draw a rectangle region around the area and press ENTER.")
        return (x, y, w, h)
    
    def _get_mouse_roi(self, image):
        """
        Calls cv2.selectROI to let user draw rectangle.
        """
        return cv2.selectROI("Select a region of interest",image)