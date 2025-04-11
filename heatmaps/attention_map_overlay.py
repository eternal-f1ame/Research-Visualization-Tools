"""
Attention Map Overlay on Image
"""
import matplotlib.pyplot as plt
import numpy as np

def overlay_attention_map(image, attention_map, alpha=0.6, title="Attention Map Overlay"):
    plt.figure(figsize=(8, 6))
    plt.imshow(image, cmap='gray')
    plt.imshow(attention_map, cmap='jet', alpha=alpha)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()