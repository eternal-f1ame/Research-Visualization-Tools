"""
Multi-Series Line Plot
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_multi_series(x, y_series, labels, title="Multi-Series Line Plot", xlabel="Epoch", ylabel="Metric"):
    fig, ax = plt.subplots()
    for y, label in zip(y_series, labels):
        ax.plot(x, y, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()