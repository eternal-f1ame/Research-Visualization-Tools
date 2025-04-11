"""
Image Cloud (Tiled Grid of Images)
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_image_cloud(images, rows=None, cols=None, title="Image Cloud"):
    n_images = len(images)
    if rows is None and cols is None:
        cols = int(np.ceil(np.sqrt(n_images)))
        rows = int(np.ceil(n_images / cols))
    elif rows is None:
        rows = int(np.ceil(n_images / cols))
    elif cols is None:
        cols = int(np.ceil(n_images / rows))

    fig, axes = plt.subplots(rows, cols, figsize=(cols*2, rows*2))
    axes = axes.flatten()

    for i in range(rows * cols):
        if i < n_images:
            axes[i].imshow(images[i])
            axes[i].axis("off")
        else:
            axes[i].remove()

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()
