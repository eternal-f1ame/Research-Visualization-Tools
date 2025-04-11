"""
Shaded Line Plot (Mean ± Std)
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_shaded_line(x, y_mean, y_std, label="Mean ± Std", color="blue", alpha=0.3, title="Shaded Line Plot"):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y_mean, label=label, color=color)
    plt.fill_between(x, y_mean - y_std, y_mean + y_std, alpha=alpha, color=color)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
