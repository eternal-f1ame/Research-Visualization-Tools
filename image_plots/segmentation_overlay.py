"""
Segmentation Overlay on Image
"""
import matplotlib.pyplot as plt
import numpy as np

def overlay_segmentation(image, mask, alpha=0.5, title="Segmentation Overlay", mask_cmap='jet'):
    plt.figure(figsize=(8, 6))
    plt.imshow(image, cmap='gray')
    plt.imshow(mask, cmap=mask_cmap, alpha=alpha)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()