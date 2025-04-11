"""
Grouped Bar Chart
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_grouped_bar(data, labels, group_labels, title="Grouped Bar Chart", ylabel="Value"):
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    for i, group in enumerate(data):
        ax.bar(x + i*width, group, width, label=group_labels[i])

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.show()