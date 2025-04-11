"""
Training Timeline with Milestones
"""
import matplotlib.pyplot as plt

def plot_training_milestones(events, times, title="Training Milestones", xlabel="Epoch", ylabel="Milestone"):
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_title(title)

    for i, (event, time) in enumerate(zip(events, times)):
        ax.plot(time, 0.5, 'o', color='crimson')
        ax.text(time, 0.6, event, rotation=45, ha='right', va='bottom')

    ax.hlines(0.5, min(times), max(times), color='gray', linestyles='dashed')
    plt.tight_layout()
    plt.show()
