"""
Grid View for Multiple Images
"""
import matplotlib.pyplot as plt

def plot_image_grid(images, rows, cols, titles=None, title="Image Grid", cmap='gray'):
    assert len(images) == rows * cols, "Number of images must match rows*cols"
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap=cmap)
        if titles:
            ax.set_title(titles[i])
        ax.axis("off")
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()