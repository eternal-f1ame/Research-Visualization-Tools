"""
Test script to verify all visualization modules load correctly.
"""
import importlib
import os

MODULE_PATHS = [
    "bar_charts.grouped_bar",
    "bar_charts.stacked_bar",
    "bar_charts.dynamic_bar_annotated",
    "line_plots.multi_series",
    "line_plots.smoothed_curves",
    "line_plots.logscale_training_curves",
    "scatter_plots.embedding_tsne",
    "scatter_plots.clustering_colormap",
    "scatter_plots.ablation_effects",
    "heatmaps.confusion_matrix",
    "heatmaps.correlation_heatmap",
    "heatmaps.attention_map_overlay",
    "image_plots.side_by_side_comparison",
    "image_plots.grid_view",
    "image_plots.segmentation_overlay",
    "model_visuals.architecture_diagram_templates",
    "model_visuals.layerwise_activation",
    "model_visuals.transformer_attention_heads",
    "utils.plot_styler",
    "utils.color_palettes",
    "utils.save_figures"
]

def test_module_imports():
    success = True
    for module in MODULE_PATHS:
        try:
            importlib.import_module(f"research_viz_kit.{module}")
            print(f"✅ {module} imported successfully.")
        except Exception as e:
            print(f"❌ Failed to import {module}: {e}")
            success = False
    return success

if __name__ == "__main__":
    result = test_module_imports()
    print("\\nAll module import tests completed." if result else "\\nSome modules failed to import.")