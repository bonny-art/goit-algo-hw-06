"""
Модуль для візуалізації графів транспортних мереж з використанням бібліотек matplotlib і networkx.

Функції:
- visualize_graph: Візуалізує граф з можливістю відображення відстані або часу.
- visualize_path_on_graph: Візуалізує шлях на графі з стрілками між вузлами.
"""

import os
import matplotlib.pyplot as plt
import networkx as nx
from graph03.utils import find_adjusted_positions

def visualize_graph(
    graph,
    weight_type='distance',
    output_dir='results',
    filename='transport_network_graph'
):
    """Візуалізація графа та збереження зображення у файл.

    Параметри:
    graph (nx.Graph): Граф для візуалізації.
    weight_type (str): Тип ваги ('distance' або 'time') для позначення на краях графа.
    output_dir (str): Директорія для збереження графіка.
    filename (str): Ім'я файлу для збереження графіка.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes,
        node_color='lightblue', font_size=9, font_weight='bold', edge_color='gray'
    )

    if weight_type == 'distance':
        edge_labels = nx.get_edge_attributes(graph, 'distance')
        label = "Відстань (км)"
    elif weight_type == 'time':
        edge_labels = nx.get_edge_attributes(graph, 'time')
        label = "Час (год)"
    elif weight_type == 'third_weight':
        edge_labels = nx.get_edge_attributes(graph, 'third_weight')
        label = "Оптимізована вага"
    else:
        raise ValueError("weight_type must be either 'distance', 'time' or 'third_weight'.")

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    plt.suptitle(f"Транспортна мережа міста\n{label}", size=20)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()

def visualize_path_on_weighted_graph(
    graph,
    path_nodes,
    output_dir='results',
    filename='path_graph',
    weight_type='distance'
):
    """Візуалізація шляху на графі.

    Параметри:
    graph (nx.Graph): Граф, на якому відображається шлях.
    path_nodes (list): Список вузлів, які формують шлях.
    output_dir (str): Директорія для збереження графіка.
    filename (str): Ім'я файлу для збереження графіка.
    title (str): Заголовок для графіка.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes,
        node_color='lightblue', font_size=9, font_weight='bold', edge_color='gray'
    )

    path_edges = [(path_nodes[i], path_nodes[i + 1]) for i in range(len(path_nodes) - 1)]

    for edge in path_edges:
        start, end = edge
        start_pos = pos[start]
        end_pos = pos[end]

        small = 0.028
        diff = 0.006

        start_size = graph.degree(start) * diff + small
        end_size = graph.degree(end) * diff + small

        adjusted_start_pos, adjusted_end_pos = find_adjusted_positions(start_pos, end_pos, start_size, end_size)

        arrow = plt.Arrow(
            adjusted_start_pos[0], adjusted_start_pos[1],
            adjusted_end_pos[0] - adjusted_start_pos[0],
            adjusted_end_pos[1] - adjusted_start_pos[1],
            width=0.02, color='red'
        )
        plt.gca().add_patch(arrow)

    if weight_type == 'distance':
        edge_labels = nx.get_edge_attributes(graph, 'distance')
        label = "Відстань (км)"
    elif weight_type == 'time':
        edge_labels = nx.get_edge_attributes(graph, 'time')
        label = "Час (год)"
    elif weight_type == 'third_weight':
        edge_labels = nx.get_edge_attributes(graph, 'third_weight')
        label = "Оптимізована вага"
    else:
        raise ValueError("weight_type must be either 'distance', 'time' or 'third_weight'.")

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    plt.suptitle(f"Транспортна мережа міста\n{label}", size=20)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()
