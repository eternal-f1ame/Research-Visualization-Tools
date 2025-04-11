"""
Cumulative Distribution Function Plot
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_cdf(data_series, labels, title="Cumulative Distribution Plot", xlabel="Value", ylabel="Cumulative Probability"):
    plt.figure(figsize=(8, 6))
    for data, label in zip(data_series, labels):
        sorted_data = np.sort(data)
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        plt.plot(sorted_data, cdf, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
