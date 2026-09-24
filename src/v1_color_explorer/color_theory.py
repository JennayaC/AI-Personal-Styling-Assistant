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