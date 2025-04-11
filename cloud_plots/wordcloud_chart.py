"""
Word Cloud Chart
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud(text, title="Word Cloud", max_words=100, background_color="white", colormap="viridis"):
    wordcloud = WordCloud(width=800, height=400, max_words=max_words,
                          background_color=background_color, colormap=colormap).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    plt.show()
