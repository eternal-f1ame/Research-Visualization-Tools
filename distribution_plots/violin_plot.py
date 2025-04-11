"""
Violin Plot for Distribution Visualization
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_violin(data, labels, title="Violin Plot", ylabel="Value"):
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=data)
    plt.xticks(ticks=range(len(labels)), labels=labels)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
