"""
t-SNE Embedding Scatter Plot
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_tsne(embeddings, labels, title="t-SNE Visualization", palette="tab10"):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=embeddings[:, 0], y=embeddings[:, 1], hue=labels, palette=palette, s=60, edgecolor="k")
    plt.title(title)
    plt.legend(title="Class")
    plt.tight_layout()
    plt.show()