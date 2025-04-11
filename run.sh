#!/bin/bash

mkdir -p {bar_charts,line_plots,scatter_plots,heatmaps,image_plots,model_visuals,utils,tests}

# Create placeholder Python files
touch bar_charts/{grouped_bar.py,stacked_bar.py,dynamic_bar_annotated.py}
touch line_plots/{multi_series.py,smoothed_curves.py,logscale_training_curves.py}
touch scatter_plots/{embedding_tsne.py,clustering_colormap.py,ablation_effects.py}
touch heatmaps/{confusion_matrix.py,correlation_heatmap.py,attention_map_overlay.py}
touch image_plots/{side_by_side_comparison.py,grid_view.py,segmentation_overlay.py}
touch model_visuals/{architecture_diagram_templates.py,layerwise_activation.py,transformer_attention_heads.py}
touch utils/{plot_styler.py,color_palettes.py,save_figures.py}
touch tests/test_all_visuals.py

# Create top-level files
touch README.md
touch requirements.txt

echo "✅ Project structure for research-viz-kit created successfully!"
