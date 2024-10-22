"""
Модуль для візуалізації транспортної мережі з використанням бібліотек Matplotlib та NetworkX.

Цей модуль містить функцію для побудови графа транспортної мережі, що демонструє обраний шлях
між вузлами за допомогою червоних стрілок, а також зберігає граф у файл.
"""

import os
import matplotlib.pyplot as plt
import networkx as nx
from graph02.utils import find_adjusted_positions

def visualize_path_on_graph(
    graph: nx.Graph,
    path_nodes: list,
    output_dir: str = 'results',
    filename: str = 'transport_network_graph',
    title: str = 'Транспортна мережа міста'
) -> None:
    """
    Візуалізація графа транспортної мережі з промальовуванням шляху червоними стрілками
    та збереженням зображення у файл.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.
        path_nodes (list): Список вершин, що визначає шлях для промальовування.
        output_dir (str): Директорія, куди зберігати зображення.
        filename (str): Назва файлу без розширення.
        title (str): Назва графа для відображення на зображенні.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)  # Позиціонування вузлів

    # Обчислюємо розміри вузлів пропорційно до їх ступеня
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    # Малюємо граф без шляху
    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes,
        node_color='lightblue', font_size=9, font_weight='bold',
        edge_color='gray'
    )

    # Створюємо список ребер на основі шляху
    path_edges = [(path_nodes[i], path_nodes[i + 1]) for i in range(len(path_nodes) - 1)]

    # Малюємо червоні стрілки для ребер зі списку
    for edge in path_edges:
        start, end = edge
        start_pos = pos[start]
        end_pos = pos[end]

        small = 0.028
        diff = 0.006

        # Обчислюємо довжину стрілки, зменшуючи її пропорційно до розмірів вузлів
        start_size = graph.degree(start) * diff + small
        end_size = graph.degree(end) * diff + small

        adjusted_start_pos, adjusted_end_pos = find_adjusted_positions(
            start_pos, end_pos, start_size, end_size
        )

        arrow = plt.Arrow(
            adjusted_start_pos[0], adjusted_start_pos[1],
            adjusted_end_pos[0] - adjusted_start_pos[0],
            adjusted_end_pos[1] - adjusted_start_pos[1],
            width=0.02, color='red'
        )
        plt.gca().add_patch(arrow)

    plt.suptitle(title, size=20)

    # Створення директорії, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Додаємо розширення .png до назви файлу
    filepath = os.path.join(output_dir, f"{filename}.png")

    # Збереження зображення графа у файл
    plt.savefig(filepath, format='png')
    plt.close()
