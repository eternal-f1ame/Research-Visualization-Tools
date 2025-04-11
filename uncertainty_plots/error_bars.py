"""
Error Bar Plot
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_error_bars(x, y, yerr, xlabel="X", ylabel="Y", title="Error Bar Plot"):
    plt.figure(figsize=(8, 6))
    plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, color='teal', ecolor='gray')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
