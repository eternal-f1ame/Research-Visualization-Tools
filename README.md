# 🧠 Research Viz Kit

A modular toolkit for generating high-quality, publication-ready visualizations — tailored for deep learning, computer vision, and robotics research.

## ✨ Features

- Consistent styling and export across all plot types
- Modular scripts for:
  - Training curves and ablations
  - Attention maps and segmentation overlays
  - Embedding visualizations (t-SNE, PCA)
  - Architecture diagrams and layer activations
  - Distribution, uncertainty, and combo plots
  - Word clouds and image grids
  - Dataset statistics and confusion matrices

## 📁 Folder Structure

```
research-viz-kit/
├── bar_charts/             # Grouped, stacked, and annotated bars
├── line_plots/             # Training dynamics, smoothed and log-scale plots
├── scatter_plots/          # Embedding spaces and ablation studies
├── heatmaps/               # Confusion matrices and attention maps
├── image_plots/            # Image grid, overlay, comparison utilities
├── model_visuals/          # Architecture & transformer insight tools
├── combo_plots/            # Bar-line overlays, twin-axis, metric overlays
├── uncertainty_plots/      # Error bars, shaded std lines, boxplots
├── radar_charts/           # Comparative radar / spider plots
├── distribution_plots/     # Violin, histogram overlay, and CDFs
├── timeline_plots/         # Step-wise accuracy and annotated training events
├── cloud_plots/            # Word clouds and image tile maps
├── utils/                  # Styling, color palettes, and save helpers
├── tests/                  # Import and smoke tests
├── README.md
└── requirements.txt
```

## 🛠 Example Usage

```python
from combo_plots.bar_line_combo import plot_bar_line_combo
from uncertainty_plots.shaded_line import plot_shaded_line
from radar_charts.comparative_radar import plot_comparative_radar
from cloud_plots.wordcloud_chart import plot_wordcloud
```

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional (for architecture diagrams):

```bash
sudo apt install graphviz
pip install graphviz wordcloud
```

## 🧪 Run Tests

```bash
python tests/test_all_visuals.py
```

---
