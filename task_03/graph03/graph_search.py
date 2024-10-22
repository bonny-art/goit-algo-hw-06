"""
Модуль для реалізації алгоритму Дейкстри з використанням бібліотеки NetworkX.

Цей модуль містить функцію для знаходження найкоротших шляхів у графі,
використовуючи алгоритм Дейкстри, з можливістю вибору метрики:
відстань або час.
"""

from typing import Dict, List, Tuple
import networkx as nx

def dijkstra(
    graph: nx.Graph,
    start: any,
    metric_type: str = 'distance'
) -> Tuple[Dict[any, float], Dict[any, List[any]]]:
    """
    Використання алгоритму Дейкстри для знаходження найкоротших шляхів.

    Args:
        graph (nx.Graph): Вхідний граф, в якому виконуються обчислення.
        start (any): Вершина, з якої починається пошук.
        metric_type (str): Тип метрики, за якою буде виконуватись пошук.
            Може бути 'distance' або 'time'.

    Returns:
        Tuple[Dict[any, float], Dict[any, List[any]]]: 
            - Словник з найкороткими відстанями до всіх вершин.
            - Словник, що містить найкоротші шляхи до всіх вершин.
    
    Raises:
        ValueError: Якщо metric_type не є 'distance' або 'time'.
    """
    if metric_type not in ['distance', 'time', 'third_weight']:
        raise ValueError("metric_type must be either 'distance' or 'time'")

    path_metrics, paths = nx.single_source_dijkstra(graph, start, weight=metric_type)
    return path_metrics, paths
