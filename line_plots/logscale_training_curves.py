"""
Log-Scale Training Curves
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_logscale_training(x, y_series, labels, title="Log-Scale Training Curves", xlabel="Epoch", ylabel="Loss"):
    fig, ax = plt.subplots()
    for y, label in zip(y_series, labels):
        ax.plot(x, y, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_yscale('log')
    ax.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()