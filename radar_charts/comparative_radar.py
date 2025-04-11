"""
Radar Chart for Multiple Models
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_comparative_radar(metrics, model_data, model_labels, colors=None, title="Comparative Radar Chart"):
    N = len(metrics)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for i, values in enumerate(model_data):
        data = values + values[:1]
        color = colors[i] if colors else None
        ax.plot(angles, data, label=model_labels[i], linewidth=2, color=color)
        ax.fill(angles, data, alpha=0.15, color=color)

    ax.set_thetagrids(np.degrees(angles[:-1]), metrics)
    ax.set_title(title)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.tight_layout()
    plt.show()
