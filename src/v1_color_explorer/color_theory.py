from src.v1_color_explorer.models import Color, ColorRelationship

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

def is_complementary(colors:list[Color], target: float = 180.0, tolerance: float = 15.0) -> bool:
    """Determines if a list of colors is complementary
    
    Args:
        colors: A list of colors to check.
        
    Returns:
        True if the colors are complementary, False otherwise.
    """
    if len(colors) != 2:
        return False
    
    base_hue = colors[0].hsl[0]

    for color in colors[1:]:
        if abs(hue_distance(base_hue, color.hsl[0]) - target) >= tolerance:
            return False
    return True

def is_triadic(colors:list[Color], target: float = 120.0, tolerance: float = 15.0) -> bool:
    """Determines if a list of colors is triadic
    
    Args:
        colors: A list of colors to check.
        
    Returns:
        True if the colors are triadic, False otherwise.
    """
    if len(colors) != 3:
        return False
    
    base_hue = colors[0].hsl[0]
    h1 = colors[1].hsl[0]
    h2 = colors[2].hsl[0]

    distance_1 = hue_distance(base_hue, h1)
    distance_2 = hue_distance(h1, h2)
    distance_3 = hue_distance(h2, base_hue)

    if abs(distance_1 - target) >= tolerance:
        return False
    if abs(distance_2 - target) >= tolerance:
        return False
    if abs(distance_3 - target) >= tolerance:
        return False
    return True

def analyze(colors: list[Color]) -> ColorRelationship:
    """Analyzes a list of colors and determines the color relationship
    
    Args:
        colors: A list of colors to check.
        
    Returns:
        The color relationship.
    """
    if is_monochromatic(colors):
        return ColorRelationship("monochromatic", "The colors are monochromatic")
    elif is_analogous(colors):
        return ColorRelationship("analogous", "The colors are analogous")
    elif is_complementary(colors):
        return ColorRelationship("complementary", "The colors are complementary")
    elif is_triadic(colors):
        return ColorRelationship("triadic", "The colors are triadic")
    else:
        return ColorRelationship("unknown", "The colors are not a recognized color relationship")



