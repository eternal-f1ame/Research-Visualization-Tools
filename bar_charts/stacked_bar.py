"""
Stacked Bar Chart
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_stacked_bar(data, labels, category_labels, title="Stacked Bar Chart", ylabel="Value"):
    x = np.arange(len(labels))
    fig, ax = plt.subplots()

    bottom = np.zeros(len(labels))
    for i, category in enumerate(data):
        ax.bar(x, category, label=category_labels[i], bottom=bottom)
        bottom += category

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.show()