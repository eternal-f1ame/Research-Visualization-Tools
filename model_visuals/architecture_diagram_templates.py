"""
Architecture Diagram Template using Graphviz
"""
from graphviz import Digraph

def draw_model_architecture():
    dot = Digraph(comment='Model Architecture')
    dot.attr(rankdir='LR')

    dot.node('I', 'Input')
    dot.node('E', 'Encoder')
    dot.node('D', 'Decoder')
    dot.node('O', 'Output')

    dot.edges(['IE', 'ED', 'DO'])

    return dot