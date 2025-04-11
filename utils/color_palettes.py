"""
Standard Color Palettes
"""
import seaborn as sns

def get_palette(name="colorblind", n_colors=10):
    return sns.color_palette(name, n_colors=n_colors)