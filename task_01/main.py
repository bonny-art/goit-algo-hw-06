"""
Модуль для створення, візуалізації та аналізу графа транспортної мережі.

Цей модуль включає:
1. Імпорт ребер для побудови графа.
2. Використання функцій для створення, візуалізації та аналізу графа.
"""

from typing import Any

from graph01.graph_creation import create_transport_network_graph
from graph01.graph_visualization import visualize_graph
from graph01.graph_analysis import analyze_graph, print_analysis_results

from edges import edges

def main() -> None:
    """
    Головна функція для створення, візуалізації та аналізу графа транспортної мережі.

    - Створює граф на основі наданих ребер.
    - Візуалізує граф та зберігає його в зазначеній директорії.
    - Виконує аналіз графа та виводить результати аналізу.

    Args:
        Немає.
    
    Returns:
        Немає.
    """
    # Створення графа транспортної мережі
    transport_network_graph: Any = create_transport_network_graph(edges)

    # Візуалізація графа з можливістю передачі назви файлу та папки
    visualize_graph(
        transport_network_graph,
        output_dir='task_01/results',
        filename='transport_network_graph'
    )

    # Аналіз графа транспортної мережі
    analysis_results: dict = analyze_graph(transport_network_graph)

    # Виведення результатів аналізу
    print_analysis_results(analysis_results)

if __name__ == "__main__":
    main()
