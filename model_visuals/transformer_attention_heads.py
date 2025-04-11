"""
Transformer Attention Heads Visualization
"""
import matplotlib.pyplot as plt
import numpy as np

def visualize_attention_heads(attention, tokens=None, title="Transformer Attention Heads"):
    num_heads = attention.shape[0]
    fig, axes = plt.subplots(1, num_heads, figsize=(4 * num_heads, 4))

    for i in range(num_heads):
        ax = axes[i] if num_heads > 1 else axes
        ax.imshow(attention[i], cmap='viridis')
        ax.set_title(f'Head {i+1}')
        if tokens:
            ax.set_xticks(np.arange(len(tokens)))
            ax.set_yticks(np.arange(len(tokens)))
            ax.set_xticklabels(tokens, rotation=90)
            ax.set_yticklabels(tokens)
        ax.grid(False)
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()