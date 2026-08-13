from dataclasses import dataclass

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
    
    label: str
    description: str


