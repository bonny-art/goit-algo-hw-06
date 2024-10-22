"""
Модуль для створення та аналізу графу транспортної мережі.
Цей модуль містить функцію для створення графа на основі з'єднань з вагами,
а також функцію для додавання третьої ваги, що враховує час і відстань.
"""

from typing import List, Tuple, Dict
import networkx as nx

def create_transport_network_graph(edges: List[Tuple[str, str, Dict[str, float]]]) -> nx.Graph:
    """
    Створює граф транспортної мережі на основі заданих з'єднань з вагами.

    :param edges: Список з'єднань, де кожне з'єднання представляє собою кортеж,
                  що містить два вузли та словник з вагами (distance, time).
    :return: Об'єкт графа, що представляє транспортну мережу.
    """
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph

def add_third_weight(graph: nx.Graph, alpha: float, beta: float) -> None:
    """
    Додає третю вагу до графа, яка враховує час і відстань.

    :param graph: Граф, до якого потрібно додати третю вагу.
    :param alpha: Вага для відстані.
    :param beta: Вага для часу.
    """
    for edge in graph.edges(data=True):
        distance = edge[2]['distance']
        time = edge[2]['time']
        # Обчислюємо третю вагу як зважену суму відстані та часу
        third_weight = round(alpha * distance + beta * time, 2)
        # Додаємо третю вагу до графа
        graph[edge[0]][edge[1]]['third_weight'] = third_weight

# Зразок вагових з'єднань
weighted_edges = [
    ('1', '38', {'distance': 26.3, 'time': 3.8}),
    ('2', '25', {'distance': 26.3, 'time': 2.2}),
    ('3', '26', {'distance': 24.1, 'time': 3.9}),
    ('4', '42', {'distance': 5.4, 'time': 2.5}),
    ('5', '21', {'distance': 1.3, 'time': 1.3})
]
