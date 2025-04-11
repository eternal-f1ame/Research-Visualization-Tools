"""
Basic Radar Chart for Single Model
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_basic_radar(metrics, values, title="Radar Chart", color='b'):
    N = len(metrics)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]  # repeat first value to close the circle
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, values, color=color, linewidth=2)
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), metrics)
    ax.set_title(title)
    plt.tight_layout()
    plt.show()
