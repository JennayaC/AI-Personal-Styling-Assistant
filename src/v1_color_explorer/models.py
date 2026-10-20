from dataclasses import dataclass
import colorsys

@dataclass
class Color:
    hex: str
    rgb: tuple[int, int, int]
    hsl: tuple[float, float, float]
    percentage: float

    def to_dict(self) -> dict: #Converts object to a dictionary
        """
        Returns the color as a dictionary of all the types defined above
        """

        return {
            "hex": self.hex,
            "rgb": self.rgb,
            "hsl": self.hsl,
            "percentage": self.percentage, #Stores how dominant the color is in the palette
            }

@dataclass
class ColorRelationship:
    """
    Identifies the color relationships of the palette
    """
    
    label: str #Label for the color relationship
    description: str #Description of the color relationship

def rgb_to_color(rgb: tuple[int, int, int], percentage: float = 0.0) -> Color:
    """Convert RGB tuple to Color object (hex and hsl)"""
    r, g, b = rgb

    #Format rgb to a hex string
    hex_code = f"#{r:02x}{g:02x}{b:02x}"

    #Convert rgb to hsl
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    hue = h * 360.0 #Converts hue to degrees on the color wheel 
    hsl = (hue, s, l)
    
    return Color(hex=hex_code, rgb=rgb, hsl=hsl, percentage=percentage)


