import networkx as nx
import matplotlib.pyplot as plt
import os
from collections import deque
import numpy as np

weighted_edges = [('1', '38', {'distance': 26.3, 'time': 3.8}),
                  ('2', '25', {'distance': 26.3, 'time': 2.2}),
                  ('3', '26', {'distance': 24.1, 'time': 3.9}),
                  ('4', '42', {'distance': 5.4, 'time': 2.5}),
                  ('5', '21', {'distance': 1.3, 'time': 1.3}),
                  ('6', '46', {'distance': 20.5, 'time': 3.3}),
                  ('7', '21', {'distance': 4.8, 'time': 3.9}),
                  ('8', '10', {'distance': 15.3, 'time': 3.3}),
                  ('9', '21', {'distance': 29.2, 'time': 3.1}),
                  ('10', '36', {'distance': 6.9, 'time': 2.9}),
                  ('11', '14', {'distance': 16.4, 'time': 3.6}),
                  ('12', '36', {'distance': 12.9, 'time': 1.7}),
                  ('13', '44', {'distance': 4.1, 'time': 1.7}),
                  ('14', '26', {'distance': 20.1, 'time': 2.3}),
                  ('15', '33', {'distance': 19.0, 'time': 1.7}),
                  ('16', '30', {'distance': 8.6, 'time': 3.5}),
                  ('17', '50', {'distance': 20.5, 'time': 1.9}),
                  ('18', '21', {'distance': 7.5, 'time': 2.8}),
                  ('19', '31', {'distance': 2.3, 'time': 1.2}),
                  ('20', '23', {'distance': 3.3, 'time': 2.9}),
                  ('21', '32', {'distance': 10.3, 'time': 2.8}),
                  ('22', '37', {'distance': 24.8, 'time': 2.0}),
                  ('23', '45', {'distance': 9.4, 'time': 2.6}),
                  ('24', '29', {'distance': 21.6, 'time': 2.8}),
                  ('25', '48', {'distance': 10.6, 'time': 1.2}),
                  ('26', '32', {'distance': 10.3, 'time': 1.1}),
                  ('28', '37', {'distance': 14.1, 'time': 1.7}),
                  ('28', '44', {'distance': 18.7, 'time': 1.2}),
                  ('32', '11', {'distance': 17.8, 'time': 3.1}),
                  ('30', '40', {'distance': 4.7, 'time': 3.0}),
                  ('31', '41', {'distance': 11.2, 'time': 3.0}),
                  ('32', '46', {'distance': 4.9, 'time': 1.5}),
                  ('33', '50', {'distance': 24.1, 'time': 1.3}),
                  ('34', '42', {'distance': 10.6, 'time': 3.3}),
                  ('35', '37', {'distance': 3.7, 'time': 1.1}),
                  ('36', '48', {'distance': 23.5, 'time': 3.5}),
                  ('37', '45', {'distance': 11.0, 'time': 3.0}),
                  ('38', '41', {'distance': 22.7, 'time': 1.7}),
                  ('47', '49', {'distance': 28.3, 'time': 2.6}),
                  ('40', '47', {'distance': 11.7, 'time': 1.5}),
                  ('41', '45', {'distance': 24.8, 'time': 2.1}),
                  ('42', '47', {'distance': 26.8, 'time': 3.1}),
                  ('43', '45', {'distance': 23.1, 'time': 2.1}),
                  ('44', '47', {'distance': 2.1, 'time': 1.9}),
                  ('45', '11', {'distance': 2.9, 'time': 3.9}),
                  ('46', '13', {'distance': 29.9, 'time': 1.1}),
                  ('47', '39', {'distance': 21.2, 'time': 2.9}),
                  ('48', '31', {'distance': 26.9, 'time': 1.5}),
                  ('49', '44', {'distance': 2.0, 'time': 3.0}),
                  ('50', '19', {'distance': 20.0, 'time': 2.0}),
                  ('31', '14', {'distance': 16.1, 'time': 3.7}),
                  ('11', '13', {'distance': 20.2, 'time': 2.8}),
                  ('40', '35', {'distance': 19.1, 'time': 2.2}),
                  ('40', '29', {'distance': 26.3, 'time': 2.9}),
                  ('27', '37', {'distance': 7.0, 'time': 2.8}),
                  ('28', '11', {'distance': 9.7, 'time': 1.6}),
                  ('49', '46', {'distance': 6.1, 'time': 1.2}),
                  ('41', '11', {'distance': 14.7, 'time': 1.2})]

def create_transport_network_graph(edges) -> nx.Graph:
    """Створює граф транспортної мережі на основі заданих з'єднань з вагами."""
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph

def find_adjusted_positions(start_pos, end_pos, start_size, end_size):
    """
    Знаходить дві точки на відрізку між start_pos і end_pos.
    
    Аргументи:
        start_pos (array-like): Координати початкової точки.
        end_pos (array-like): Координати кінцевої точки.
        start_size (float): Відстань від початкової точки.
        end_size (float): Відстань від кінцевої точки.
    
    Повертає:
        tuple: Дві точки (adjusted_start_pos, adjusted_end_pos).
    """
    # Обчислюємо напрямок вектора
    direction = np.array(end_pos) - np.array(start_pos)
    direction_norm = direction / np.linalg.norm(direction)

    # Знаходимо нові позиції
    adjusted_start_pos = np.array(start_pos) + direction_norm * start_size
    adjusted_end_pos = np.array(end_pos) - direction_norm * end_size

    return adjusted_start_pos, adjusted_end_pos

def visualize_graph(graph, weight_type='distance', output_dir='results', filename='transport_network_graph'):
    """
    Візуалізація графа транспортної мережі та збереження зображення у файл.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.
        use_distance (bool): Якщо True, відстань буде використана для міток ребер, інакше - час.
        output_dir (str): Директорія, куди зберігати зображення.
        filename (str): Назва файлу без розширення.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)

    # Обчислюємо розміри вузлів пропорційно до їх ступеня
    node_sizes = [500 * graph.degree(node) for node in graph.nodes()]

    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes, node_color='lightblue', font_size=9, font_weight='bold',
        edge_color='gray'
    )

    # Вибір ваг для міток ребер
    if weight_type == 'distance':
        edge_labels = nx.get_edge_attributes(graph, 'distance')
        label = "Відстань (км)"
    elif weight_type == 'time':
        edge_labels = nx.get_edge_attributes(graph, 'time')
        label = "Час (год)"
    else:
        raise ValueError("weight_type must be either 'distance' or 'time'")

    # Зменшити розмір шрифту міток на ребрах
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    # Додаємо мітку під заголовком
    plt.suptitle(f"Транспортна мережа міста\n{label}", size=20)

    # Створення директорії, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Додаємо розширення .png до назви файлу
    filepath = os.path.join(output_dir, f"{filename}.png")

    # Збереження зображення графа у файл
    plt.savefig(filepath, format='png')
    plt.close()

def visualize_path_on_graph(
    graph,
    path_nodes,
    output_dir='results',
    filename='transport_network_graph',
    title='Транспортна мережа міста'
):
    """
    Візуалізація графа транспортної мережі з промальовуванням шляху червоними стрілками
    та збереженням зображення у файл.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.
        path_nodes (list): Список вершин, що визначає шлях для промальовування червоними стрілками.
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
        graph, pos, with_labels=True, node_size=node_sizes, node_color='lightblue', font_size=9, font_weight='bold',
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

        adjusted_start_pos, adjusted_end_pos = find_adjusted_positions(start_pos, end_pos, start_size, end_size)

        arrow = plt.Arrow(adjusted_start_pos[0], adjusted_start_pos[1],
                          adjusted_end_pos[0] - adjusted_start_pos[0],
                          adjusted_end_pos[1] - adjusted_start_pos[1],
                          width=0.02, color='red')
        plt.gca().add_patch(arrow)

    # Вибір ваг для міток ребер
    if weight_type == 'distance':
        edge_labels = nx.get_edge_attributes(graph, 'distance')
        label = "Відстань (км)"
    elif weight_type == 'time':
        edge_labels = nx.get_edge_attributes(graph, 'time')
        label = "Час (год)"
    else:
        raise ValueError("weight_type must be either 'distance' or 'time'")

    # Зменшити розмір шрифту міток на ребрах
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    # Додаємо заголовок, переданий у параметрі title
    plt.suptitle(title, size=20)

    # Створення директорії, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Додаємо розширення .png до назви файлу
    filepath = os.path.join(output_dir, f"{filename}.png")

    # Збереження зображення графа у файл
    plt.savefig(filepath, format='png')
    plt.close()

def dijkstra(graph, start, metric_type='distance'):
    # Використання алгоритму Дейкстри для знаходження найкоротших шляхів
    if metric_type not in ['distance', 'time']:
        raise ValueError("metric_type must be either 'distance' or 'time'")
    
    # Розрахунок найкоротших шляхів
    path_metrics, paths = nx.single_source_dijkstra(graph, start, weight=metric_type)
    
    return path_metrics, paths

transport_graph = create_transport_network_graph(weighted_edges)

# Візуалізація графа з використанням відстані
visualize_graph(transport_graph, output_dir='task_03/results', weight_type='distance', filename='transport_network_graph_distance')
visualize_graph(transport_graph, output_dir='task_03/results', weight_type='time', filename='transport_network_graph_time')

start_node = '15'  # Ваша стартова вершина
weight_type = 'distance'  # Вибір типу ваги ('distance' або 'time')

# Виклик функції Дейкстри для відстаней
path_metrics, paths_len = dijkstra(transport_graph, start_node, metric_type='distance')
print(paths_len)

# Виведення результатів
print("\nНайкоротші відстані та шляхи від вершини:", start_node)
for node in sorted(path_metrics.keys(), key=int):  # Сортуємо ключі як цілі числа
    print(f"Вершина {node}: відстань = {path_metrics[node]:.2f}, шлях = {' -> '.join(paths_len[node])}")

start_vertex = '15'
end_vertex = '16'
path_to_visualize_len = paths_len[end_vertex]


# Викликаємо функцію
visualize_path_on_graph(transport_graph, path_to_visualize_len, output_dir='task_03/results', filename='path_15_to_16_len', title='Найкоротший шлях (відстань) від 15 до 16')



# Виклик функції Дейкстри для часу
time_metrics, paths_time = dijkstra(transport_graph, start_node, metric_type='time')


# Виведення результатів
print("\nНайкоротші часи та шляхи від вершини:", start_node)
for node in sorted(time_metrics.keys(), key=int):  # Сортуємо ключі як цілі числа
    print(f"Вершина {node}: час = {time_metrics[node]:.2f}, шлях = {' -> '.join(paths_time[node])}")

path_to_visualize_time = paths_time[end_vertex]

# Викликаємо функцію
visualize_path_on_graph(transport_graph, path_to_visualize_time, output_dir='task_03/results', filename='path_15_to_16_time', title='Нашвидший шлях (час) від 15 до 16')