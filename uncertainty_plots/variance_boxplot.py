"""
Boxplot for Variance Across Experiments
"""
import matplotlib.pyplot as plt

def plot_variance_boxplot(data, labels, title="Boxplot of Metric Variance", ylabel="Score"):
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=labels, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='blue'),
                medianprops=dict(color='black'))
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
