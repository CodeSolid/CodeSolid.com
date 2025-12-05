import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def setup_math_axes(ax=None, x_lim=(-10, 10), y_lim=(-10, 10), 
                    grid=True, equal_aspect=False):
    """
    Configures a Matplotlib axis to look like a standard math textbook graph:
    - Spines centered at (0,0).
    - Arrowheads at the ends of the axes.
    - Optional grid and equal aspect ratio.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes, optional
        The axis object to modify. If None, a new figure and axis are created.
    x_lim, y_lim : tuple
        The limits for the x and y axes (min, max).
    grid : bool
        Whether to display the grid (default: True).
    equal_aspect : bool
        If True, sets aspect ratio to 'equal' (crucial for circles/geometry).
        
    Returns:
    --------
    ax : matplotlib.axes.Axes
        The configured axis object.
    """
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))

    # 1. Set limits
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    # 2. Move left and bottom spines to zero (the origin)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # 3. Hide the top and right spines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 4. Add arrows to the ends of the axes
    # We use plot() with transform to place arrows at the absolute ends of the visible axis
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # 5. Configure Grid
    if grid:
        ax.grid(True, linestyle=':', alpha=0.6)

    # 6. Configure Aspect Ratio
    if equal_aspect:
        ax.set_aspect('equal')

    # 7. Move tick labels so they don't overlap the axes lines
    # (Optional: adjusts specific quadrants if needed, but defaults usually work well)
    
    return ax