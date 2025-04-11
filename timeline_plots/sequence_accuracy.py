"""
Per-Step Sequence Accuracy Plot
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_sequence_accuracy(steps, accuracies, title="Sequence Accuracy Over Time", xlabel="Time Step", ylabel="Accuracy"):
    plt.figure(figsize=(8, 6))
    plt.plot(steps, accuracies, marker='o', linestyle='-', color='teal')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
