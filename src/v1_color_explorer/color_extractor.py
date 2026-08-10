import numpy as np
from sklearn.cluster import KMeans 

def extract_colors(image_region: np.ndarray, n_colors: int = 5) -> list[tuple[int, int, int]]:
    """
    Extract the dominant colors from an image region using K-Means clustering.

    Args:
        image_region: A NumPy array of shape (height, width, 3) in BGR format.
        n_colors: The number of dominant colors to extract. Defaults to 5.

    Returns:
        A list of (R, G, B) tuples representing the dominant colors.
    """
    pixels = image_region.reshape(-1, 3) #The -1 tells numpy to automatically calculate the number of rows
    pixels = pixels[:, ::-1].astype(np.float32) #Flips BGR to RGB and converts values to floats for KMeans

    kmeans = KMeans(n_clusters = n_colors, n_init = "auto", random_state = 42).fit(pixels) #runs kmeans algorithm on pixels to group them into n_colors clusters

    centers = kmeans.cluster_centers_.astype(int) #gets the center of each cluster
    return [tuple(color) for color in centers] #returns the centers as a list of tuples

