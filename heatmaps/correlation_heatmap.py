"""
Correlation Heatmap
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_correlation_heatmap(dataframe, title="Correlation Heatmap"):
    plt.figure(figsize=(10, 8))
    corr = dataframe.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()