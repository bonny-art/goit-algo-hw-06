"""
Модуль для побудови та аналізу транспортної мережі станцій з використанням графів.
Включає алгоритми пошуку в глибину (DFS) та в ширину (BFS) для знаходження шляхів між станціями.
"""

import os
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

edges = [
    ('1', '38'), ('2', '25'), ('3', '26'), ('4', '42'),
    ('5', '21'), ('6', '46'), ('7', '21'), ('8', '10'),
    ('9', '21'), ('10', '36'), ('11', '14'), ('12', '36'),
    ('13', '44'), ('14', '26'), ('15', '33'), ('16', '30'),
    ('17', '50'), ('18', '21'), ('19', '31'), ('20', '23'),
    ('21', '32'), ('22', '37'), ('23', '45'), ('24', '29'),
    ('25', '48'), ('26', '32'), ('28', '37'), ('28', '44'),
    ('32', '11'), ('30', '40'), ('31', '41'), ('32', '46'),
    ('33', '50'), ('34', '42'), ('35', '37'), ('36', '48'),
    ('37', '45'), ('38', '41'), ('47', '49'), ('40', '47'),
    ('41', '45'), ('42', '47'), ('43', '45'), ('44', '47'),
    ('45', '11'), ('46', '13'), ('47', '39'), ('48', '31'),
    ('49', '44'), ('50', '19'), ('31', '14'), ('11', '13'),
    ('40', '35'), ('40', '29'), ('27', '37'), ('28', '11'),
    ('49', '46'), ('41', '11')
]

def create_transport_network_graph() -> nx.Graph:
    """Створює граф транспортної мережі на основі заданих з'єднань."""
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph

def dfs(graph: nx.Graph, start: str, goal: str, path: list = None) -> list:
    """Виконує пошук в глибину (DFS) для знаходження шляху між станціями.
    
    Аргументи:
        graph: Граф станцій.
        start: Початкова станція.
        goal: Кінцева станція.
        path: Поточний шлях (за замовчуванням None).
        
    Повертає:
        Список станцій у знайденому шляху або None, якщо шлях не знайдено.
    """
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

def bfs(graph: nx.Graph, start: str, goal: str) -> list:
    """Виконує пошук в ширину (BFS) для знаходження шляху між станціями.
    
    Аргументи:
        graph: Граф станцій.
        start: Початкова станція.
        goal: Кінцева станція.
        
    Повертає:
        Список станцій у знайденому шляху або None, якщо шлях не знайдено.
    """
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for adjacent in graph[node]:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return None

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

def main() -> None:
    """Головна функція для створення графа та знаходження шляхів між станціями."""
    graph = create_transport_network_graph()
    start_station = '15'
    goal_station = '16'

    # Пошук шляху за допомогою DFS
    dfs_path = dfs(graph, start_station, goal_station)
    if dfs_path:
        print(f"DFS шлях з {start_station} до {goal_station}: {dfs_path}")
        # Візуалізація та збереження шляху, знайденого DFS
        visualize_path_on_graph(
            graph,
            dfs_path,
            output_dir='task_02/results',
            filename='dfs_path',
            title='DFS Шлях у Транспортній Мережі'
        )

    else:
        print(f"DFS не знайшов шлях між {start_station} та {goal_station}.")

    # Пошук шляху за допомогою BFS
    bfs_path = bfs(graph, start_station, goal_station)
    if bfs_path:
        print(f"BFS шлях з {start_station} до {goal_station}: {bfs_path}")
        # Візуалізація та збереження шляху, знайденого BFS
        visualize_path_on_graph(
            graph,
            bfs_path,
            output_dir='task_02/results',
            filename='bfs_path',
            title='BFS Шлях у Транспортній Мережі'
        )
    else:
        print(f"BFS не знайшов шлях між {start_station} та {goal_station}.")

if __name__ == "__main__":
    main()
