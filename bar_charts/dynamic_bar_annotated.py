"""
Annotated Bar Chart (Dynamic Labels)
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_annotated_bar(values, labels, title="Annotated Bar Chart", ylabel="Value"):
    x = np.arange(len(labels))
    fig, ax = plt.subplots()
    bars = ax.bar(x, values)

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.show()