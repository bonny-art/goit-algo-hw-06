"""
Модуль для створення та аналізу транспортної мережі станцій.

Цей модуль імплементує пошук шляхів у графі за допомогою алгоритмів 
глибини (DFS) та ширини (BFS) та візуалізує знайдені шляхи.
"""

from graph02.graph_creation import create_transport_network_graph
from graph02.graph_search import dfs, bfs
from graph02.graph_visualization import visualize_path_on_graph

from edges import edges

def main() -> None:
    """Основна функція програми.

    Створює граф транспортної мережі, виконує пошук шляхів між
    стартовою та цільовою станцією за допомогою DFS та BFS, а також
    візуалізує знайдені шляхи.
    """
    graph = create_transport_network_graph(edges)
    start_station = '15'
    goal_station = '16'

    # Пошук шляху за допомогою DFS
    dfs_path = dfs(graph, start_station, goal_station)
    if dfs_path:
        print(f"DFS шлях з {start_station} до {goal_station}: {dfs_path}")
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
