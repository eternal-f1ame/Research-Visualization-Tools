"""
Global Plot Styler for Consistency
"""
import matplotlib.pyplot as plt

def apply_plot_style(style="seaborn-whitegrid", font_size=12, font_family="serif"):
    plt.style.use(style)
    plt.rcParams.update({
        "font.size": font_size,
        "font.family": font_family,
        "axes.titlesize": font_size + 2,
        "axes.labelsize": font_size,
        "legend.fontsize": font_size - 1,
        "xtick.labelsize": font_size - 1,
        "ytick.labelsize": font_size - 1
    })