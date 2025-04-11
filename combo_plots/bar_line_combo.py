"""
Bar + Line Combo Plot
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_bar_line_combo(bar_values, line_values, labels, bar_label="Bar", line_label="Line",
                        xlabel="X", ylabel="Primary Y", secondary_ylabel="Secondary Y",
                        title="Bar + Line Combo"):
    x = np.arange(len(labels))
    fig, ax1 = plt.subplots()

    ax1.bar(x, bar_values, color='skyblue', label=bar_label)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel, color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

    ax2 = ax1.twinx()
    ax2.plot(x, line_values, color='crimson', marker='o', label=line_label)
    ax2.set_ylabel(secondary_ylabel, color='crimson')
    ax2.tick_params(axis='y', labelcolor='crimson')

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    fig.tight_layout()
    plt.title(title)
    plt.show()
