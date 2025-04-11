"""
Scatter Plot for Ablation Effects
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_ablation_scatter(x, y, labels=None, title="Ablation Effects", xlabel="Setting", ylabel="Accuracy"):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='r', edgecolor='k')
    for i, txt in enumerate(labels or []):
        plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 5), ha='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()