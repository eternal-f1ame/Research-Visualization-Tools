"""
Clustered Scatter Plot with Color Map
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_clustered_colormap(xy_data, cluster_labels, title="Cluster Visualization"):
    x, y = xy_data[:, 0], xy_data[:, 1]
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x, y, c=cluster_labels, cmap='viridis', edgecolor='k', s=50)
    plt.colorbar(scatter, label='Cluster ID')
    plt.title(title)
    plt.tight_layout()
    plt.show()