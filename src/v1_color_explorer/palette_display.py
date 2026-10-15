import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
from src.v1_color_explorer.models import Color, ColorRelationship


def create_figure(colors: list[Color], relationship: ColorRelationship) -> plt.Figure:
    """Creates a matplotlib Figure object displaying the color palette."""
    
    fig, ax = plt.subplots(figsize=(8, 3))

    #Draw a rectangle for each swatch side by side
    for i, color in enumerate(colors):
        rect = Rectangle(xy=(i, 0), width=1.0, height=1.0, facecolor=color.hex, edgecolor="none")
        ax.add_patch(rect)

    #Make sure swatches fill entire space
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)

    #Set title with relationship label and description
    ax.set_title(f"{relationship.label.title()}: {relationship.description}", fontsize=12, pad=15)

    #Remove standard axis lines
    ax.axis("off")

    return fig

    
    