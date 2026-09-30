from src.v1_color_explorer.models import Color

def hue_distance(h1: float, h2: float) -> float:
    """Calculates the shortest distance between two hue angles in degrees (0-360)
    
    Args:
        h1: The first hue angle.
        h2: The second hue angle.
        
    Returns:
        The shortest distance between the two hue angles.
    """
    difference = abs(h1 - h2)
    return min(difference, 360.0 - difference)

def is_monochromatic(colors:list[Color], threshold = 15.0) -> bool:
    """Determines if a list of colors is monochromatic
    
    Args:
        colors: A list of colors to check.
        
    Returns:
        True if the colors are monochromatic, False otherwise.
    """
    if len(colors) <= 1:
        return True
    
    base_hue = colors[0].hsl[0]

    for color in colors[1:]:
        if hue_distance(base_hue, color.hsl[0]) > threshold:
            return False
    return True

def is_analogous(colors:list[Color], threshold = 60.0) -> bool:
    """Determines if a list of colors is analogous
    
    Args:
        colors: A list of colors to check.
        
    Returns:
        True if the colors are analogous, False otherwise.
    """
    if len(colors) <= 1:
        return True
    
    base_hue = colors[0].hsl[0]

    for color in colors[1:]:
        if hue_distance(base_hue, color.hsl[0]) > threshold:
            return False
    return True
