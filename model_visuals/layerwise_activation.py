"""
Layerwise Activation Visualization
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_layerwise_activations(activations, layer_names=None, title="Layerwise Activations"):
    num_layers = len(activations)
    fig, axes = plt.subplots(1, num_layers, figsize=(4 * num_layers, 4))
    if num_layers == 1:
        axes = [axes]

    for i, (act, ax) in enumerate(zip(activations, axes)):
        ax.imshow(act, cmap='viridis')
        ax.axis('off')
        if layer_names:
            ax.set_title(layer_names[i])
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()