# Res Vis Tools

A modular toolkit for generating high-quality, publication-ready visualizations — tailored for deep learning, computer vision, and robotics research.

## Features

- Consistent styling and export across all plot types
- Modular scripts for:
  - Training curves and ablations
  - Attention maps and segmentation overlays
  - Embedding visualizations (t-SNE, PCA)
  - Architecture diagrams and layer activations
  - Dataset statistics and confusion matrices

## Folder Structure

```bash
research-viz-kit/
├── bar_charts/             # Grouped, stacked, and annotated bars
├── line_plots/             # Training dynamics, smoothed and log-scale plots
├── scatter_plots/          # Embedding spaces and ablation studies
├── heatmaps/               # Confusion matrices and attention maps
├── image_plots/            # Image grid, overlay, comparison utilities
├── model_visuals/          # Architecture & transformer insight tools
├── utils/                  # Styling, color palettes, and save helpers
├── tests/                  # Import and smoke tests
├── README.md
└── requirements.txt
```

## Example Usage

```python
from bar_charts.grouped_bar import plot_grouped_bar
plot_grouped_bar(data=[[1, 2, 3], [2, 3, 4]], labels=['A', 'B', 'C'], group_labels=['Model X', 'Model Y'])
```

```python
from line_plots.smoothed_curves import plot_smoothed_lines
plot_smoothed_lines(x=range(10), y_series=[[0.1*i for i in range(10)], [0.2*i for i in range(10)]], labels=['Run 1', 'Run 2'])
```

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional (for architecture diagrams):

```bash
sudo apt install graphviz
pip install graphviz
```

## 🧪 Run Tests

```bash
python tests/test_all_visuals.py
```

