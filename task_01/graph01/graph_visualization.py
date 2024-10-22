"""
Модуль для візуалізації графів транспортних мереж міста.

Містить функцію `visualize_graph`, яка дозволяє візуалізувати транспортну мережу, представлену у вигляді графа,
та зберегти результат у вигляді зображення.

Використовуються бібліотеки:
- os: для роботи з файловою системою.
- matplotlib.pyplot: для побудови графіків.
- networkx: для роботи з графами.

Функціонал:
- Візуалізація графа.
- Налаштування вигляду графа (розмір вузлів залежно від ступеня).
- Збереження зображення у вказану директорію.
"""

import os
import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph: nx.Graph, output_dir: str = 'results', filename: str = 'transport_network_graph') -> None:
    """
    Візуалізація графа транспортної мережі та збереження зображення у файл.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.
        output_dir (str, optional): Директорія, куди зберігати зображення. За замовчуванням 'results'.
        filename (str, optional): Назва файлу без розширення. За замовчуванням 'transport_network_graph'.
    
    Опис:
        Функція будує граф на основі поданого об'єкта типу `networkx.Graph`. 
        Розмір вузлів масштабовано відповідно до їх ступеня (кількості з'єднань).
        Граф зберігається у вигляді PNG-зображення у вказаній директорії.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)

    # Обчислюємо розміри вузлів пропорційно до їх ступеня
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    # Візуалізація графа
    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes, node_color='lightblue', font_size=9,
        font_weight='bold', edge_color='gray'
    )

    plt.suptitle("Транспортна мережа міста", size=20)

    # Створення директорії, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Додаємо розширення .png до назви файлу
    filepath = os.path.join(output_dir, f"{filename}.png")

    # Збереження зображення графа у файл
    plt.savefig(filepath, format='png')
    plt.close()
