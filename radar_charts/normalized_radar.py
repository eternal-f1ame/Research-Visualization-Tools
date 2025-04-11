"""
Normalized Radar Chart (0-1 Scaling)
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_normalized_radar(metrics, model_data, model_labels, title="Normalized Radar Chart"):
    # Normalize all values to 0-1 range
    model_data = np.array(model_data)
    min_vals = model_data.min(axis=0)
    max_vals = model_data.max(axis=0)
    norm_data = (model_data - min_vals) / (max_vals - min_vals + 1e-8)

    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for i, values in enumerate(norm_data):
        data = values.tolist() + [values[0]]
        ax.plot(angles, data, label=model_labels[i])
        ax.fill(angles, data, alpha=0.15)

    ax.set_thetagrids(np.degrees(angles[:-1]), metrics)
    ax.set_title(title)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.tight_layout()
    plt.show()
