"""
Модуль для аналізу графа транспортної мережі.

Цей модуль надає функціонал для аналізу характеристик графа, що представляє транспортну мережу міста.
Він містить дві основні функції: `analyze_graph` для проведення аналізу та `print_analysis_results`
для виведення результатів аналізу на екран.

Використання:
    - analyze_graph(graph: nx.Graph) -> dict: аналізує транспортну мережу та повертає словник з результатами.
    - print_analysis_results(analysis_results: dict) -> None: виводить результати аналізу графа.
"""

from typing import Dict
import networkx as nx

def analyze_graph(graph: nx.Graph) -> Dict:
    """
    Аналіз характеристик графа транспортної мережі.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.

    Повертає:
        Dict: Словник з характеристиками графа.
    """
    analysis_results = {}

    # Підрахунок основних характеристик графа
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    degree_distribution = [graph.degree(n) for n in graph.nodes()]

    # Підрахунок кількості вершин для кожного ступеня
    degree_count = {}
    for node in graph.nodes():
        degree = graph.degree(node)
        if degree in degree_count:
            degree_count[degree] += 1
        else:
            degree_count[degree] = 1

    # Збереження результатів аналізу
    analysis_results['num_nodes'] = num_nodes
    analysis_results['num_edges'] = num_edges
    analysis_results['degree_distribution'] = degree_distribution
    analysis_results['degree_count'] = degree_count
    analysis_results['average_degree'] = sum(degree_distribution) / num_nodes
    analysis_results['connected_components'] = nx.number_connected_components(graph)

    # Перевірка, чи граф зв'язаний, перед обчисленням діаметра та середньої довжини найкоротшого шляху
    if nx.is_connected(graph):
        analysis_results['diameter'] = nx.diameter(graph)
        analysis_results['average_shortest_path_length'] = nx.average_shortest_path_length(graph)
    else:
        analysis_results['diameter'] = None
        analysis_results['average_shortest_path_length'] = None

    return analysis_results


def print_analysis_results(analysis_results: Dict) -> None:
    """
    Виведення результатів аналізу графа.

    Аргументи:
        analysis_results (Dict): Словник з характеристиками графа.
    """
    print("\nАналіз характеристик графа Транспортна мережа міста:")
    print("\nЗбережене зображення графа: results/transport_network_graph.png")
    print(f"\nКількість станцій (Вершин): {analysis_results['num_nodes']}")
    print(f"Кількість з'єднань (Ребер): {analysis_results['num_edges']}")
    print(f"\nРозподіл ступенів: {analysis_results['degree_distribution']}\n")

    for degree, count in analysis_results['degree_count'].items():
        print(f"Кількість вершин, що мають {degree} ребро(-ів): {count}")

    print(f"\nСередній ступінь: {analysis_results['average_degree']:.2f}")
    print(f"Кількість зв'язаних компонент: {analysis_results['connected_components']}")

    if analysis_results['diameter'] is not None:
        print(f"Діаметр графа: {analysis_results['diameter']}")
        print(f"Середня довжина найкоротшого шляху: {analysis_results['average_shortest_path_length']:.2f}\n")
    else:
        print("Граф не є зв'язним, тому діаметр і середню довжину шляху неможливо обчислити.\n")
