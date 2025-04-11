"""
Overlayed Histograms
"""
import matplotlib.pyplot as plt

def plot_histogram_overlay(data_series, labels, bins=20, alpha=0.5, title="Histogram Overlay", xlabel="Value", ylabel="Frequency"):
    plt.figure(figsize=(8, 6))
    for data, label in zip(data_series, labels):
        plt.hist(data, bins=bins, alpha=alpha, label=label, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()
