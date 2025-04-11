"""
Smoothed Line Curves
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

def plot_smoothed_lines(x, y_series, labels, sigma=2, title="Smoothed Line Plot", xlabel="Epoch", ylabel="Metric"):
    fig, ax = plt.subplots()
    for y, label in zip(y_series, labels):
        y_smoothed = gaussian_filter1d(y, sigma=sigma)
        ax.plot(x, y_smoothed, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()