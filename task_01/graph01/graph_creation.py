"""
Модуль для створення графа транспортної мережі міста з використанням бібліотеки NetworkX.

Містить функції для побудови графа та додавання з'єднань між транспортними станціями.
"""

from typing import List, Tuple
import networkx as nx

def create_transport_network_graph(edges: List[Tuple[str, str]]) -> nx.Graph:
    """
    Створює граф транспортної мережі міста, додаючи станції та їх з'єднання.

    Параметри:
        edges (List[Tuple[str, str]]): Список ребер, де кожне ребро є парою станцій (назви станцій).

    Повертає:
        nx.Graph: Граф, що представляє транспортну мережу.
    """
    # Створення пустого графа
    graph = nx.Graph()

    # Додавання ребер до графа
    graph.add_edges_from(edges)

    return graph
