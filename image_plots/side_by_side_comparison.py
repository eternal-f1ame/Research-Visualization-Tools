"""
Side-by-Side Image Comparison
"""
import matplotlib.pyplot as plt

def plot_side_by_side(images, titles=None, title="Comparison", cmap='gray'):
    num_images = len(images)
    plt.figure(figsize=(5 * num_images, 5))
    for i, img in enumerate(images):
        plt.subplot(1, num_images, i + 1)
        plt.imshow(img, cmap=cmap)
        if titles:
            plt.title(titles[i])
        plt.axis("off")
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()