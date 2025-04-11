"""
Save Figures in Multiple Formats
"""
import os
import matplotlib.pyplot as plt

def save_figure(name, folder="figures", formats=("png", "pdf", "eps"), dpi=300):
    os.makedirs(folder, exist_ok=True)
    for fmt in formats:
        path = os.path.join(folder, f"{name}.{fmt}")
        plt.savefig(path, format=fmt, dpi=dpi, bbox_inches='tight')
    print(f"Figure saved to {folder} as {formats}")