import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def annotate_bars(ax):
    """
    Annotate bars in a bar plot with their values.

    Parameters:
    - ax (matplotlib.axes.Axes): The axes object representing the bar plot.
    """
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.0f}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            fontsize=8,
            color="black",
            xytext=(0, 10),
            textcoords="offset points",
        )


def format_millions(x, pos):
    """
    Format a numeric value in millions with one decimal place and add '$' sign.

    Parameters:
    - x (float): The numeric value.
    - pos (int): The tick position.

    Returns:
    str: The formatted value.
    """
    return f"${x / 1e6:.1f}M"
