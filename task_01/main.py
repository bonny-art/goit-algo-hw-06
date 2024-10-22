"""
Модуль для аналізу та візуалізації транспортної мережі міста за допомогою графів.

Цей скрипт створює граф, що представляє станції та з'єднання між ними, візуалізує його,
зберігає зображення графа та проводить аналіз його характеристик.

Використовуються бібліотеки:
- NetworkX для роботи з графами.
- Matplotlib для візуалізації графів.
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def create_transport_network_graph():
    """
    Створення графа транспортної мережі міста та додавання станцій і з'єднань.

    Повертає:
        nx.Graph: Граф, що представляє транспортну мережу.
    """
    # Створення графа
    graph = nx.Graph()

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

    graph.add_edges_from(edges)

    return graph

def visualize_graph(graph, output_dir='results', filename='transport_network_graph'):
    """
    Візуалізація графа транспортної мережі та збереження зображення у файл.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.
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

    plt.suptitle("Транспортна мережа міста", size=20)

    # Створення директорії, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Додаємо розширення .png до назви файлу
    filepath = os.path.join(output_dir, f"{filename}.png")

    # Збереження зображення графа у файл
    plt.savefig(filepath, format='png')
    plt.close()


def analyze_graph(graph):
    """
    Аналіз характеристик графа транспортної мережі.

    Аргументи:
        graph (nx.Graph): Граф, що представляє транспортну мережу.

    Повертає:
        dict: Словник з характеристиками графа.
    """
    analysis_results = {}

    # Аналіз характеристик
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

    # Збереження результатів
    analysis_results['num_nodes'] = num_nodes
    analysis_results['num_edges'] = num_edges
    analysis_results['degree_distribution'] = degree_distribution
    analysis_results['degree_count'] = degree_count
    analysis_results['average_degree'] = sum(degree_distribution) / num_nodes
    analysis_results['connected_components'] = nx.number_connected_components(graph)
    analysis_results['diameter'] = nx.diameter(graph)
    analysis_results['average_shortest_path_length'] = nx.average_shortest_path_length(graph)

    return analysis_results

def print_analysis_results(analysis_results):
    """
    Виведення результатів аналізу графа.

    Аргументи:
        analysis_results (dict): Словник з характеристиками графа.
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
    print(f"Діаметр графа: {analysis_results['diameter']}")
    print(f"Середня довжина найкоротшого шляху: {analysis_results['average_shortest_path_length']:.2f}\n")

def main():
    """
    Головна функція для створення, візуалізації та аналізу графа транспортної мережі.
    """
    # Створення графа
    transport_network_graph = create_transport_network_graph()

    # Візуалізація графа з можливістю передачі назви файлу та папки
    visualize_graph(transport_network_graph, output_dir='task_01/results', filename='transport_network_graph')

    # Аналіз графа
    analysis_results = analyze_graph(transport_network_graph)

    # Виведення результатів
    print_analysis_results(analysis_results)

if __name__ == "__main__":
    main()
