"""
Multi-Metric Overlay Line Plot
"""
import matplotlib.pyplot as plt

def plot_multi_metric(x, metrics, labels, xlabel="Epoch", ylabel="Score", title="Multi-Metric Overlay"):
    fig, ax = plt.subplots()
    for y, label in zip(metrics, labels):
        ax.plot(x, y, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
