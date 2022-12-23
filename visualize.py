import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
from structure.node import Node


def draw_graph(root: Node, graph: nx.Graph) -> nx.Graph:
    """function to draw the graph of the given root"""
    graph.add_node(root.id, value=root.data)
    if root.left:
        left_side = draw_graph(root.left, graph)
        graph.add_edge(root.id, root.left.id)

    if root.right:
        right_side = draw_graph(root.right, graph)
        graph.add_edge(root.id, root.right.id)
    return graph


def show_graph(root: Node) -> None:
    """function to visualize the graph"""
    graph = draw_graph(root, nx.Graph())
    pos = graphviz_layout(graph, prog="dot")
    labels = nx.get_node_attributes(graph, 'value')
    nx.draw(graph, pos, labels=labels, with_labels=True)
    plt.show()
