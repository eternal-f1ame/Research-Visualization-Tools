"""
Twin Axis Line Plot
"""
import matplotlib.pyplot as plt

def plot_twin_axis(x, y1, y2, label1="Left Y", label2="Right Y", xlabel="X", title="Twin Axis Plot"):
    fig, ax1 = plt.subplots()

    ax1.plot(x, y1, 'b-', label=label1)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(label1, color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'r--', label=label2)
    ax2.set_ylabel(label2, color='r')
    ax2.tick_params('y', colors='r')

    plt.title(title)
    fig.tight_layout()
    plt.show()
