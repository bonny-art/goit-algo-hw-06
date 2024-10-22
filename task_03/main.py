"""
Модуль для створення, візуалізації та пошуку в транспортній мережі.

Цей модуль імплементує функції для створення графа транспортної мережі, 
візуалізації графа та виконання алгоритму Дейкстри для пошуку найкоротших шляхів.
"""

from edges import weighted_edges

from graph03.graph_creation import create_transport_network_graph, add_third_weight
from graph03.graph_visualization import visualize_graph, visualize_path_on_weighted_graph
from graph03.graph_search import dijkstra

# Створюємо граф
transport_graph = create_transport_network_graph(weighted_edges)

# Додаємо третю вагу до графа
add_third_weight(transport_graph, alpha=0.4, beta=0.6)

# Візуалізація графа з використанням відстані, часу та оптимізованої ваги
visualize_graph(
    transport_graph,
    output_dir='task_03/results',
    weight_type='distance',
    filename='transport_network_graph_distance'
)
visualize_graph(
    transport_graph,
    output_dir='task_03/results',
    weight_type='time',
    filename='transport_network_graph_time'
)
visualize_graph(
    transport_graph,
    output_dir='task_03/results',
    weight_type='third_weight',
    filename='transport_network_graph_optimized'
)

START_NODE = '15'
END_VERTEX = '16'

#######################################################
# Виклик функції Дейкстри для відстаней
path_metrics, paths_len = dijkstra(transport_graph, START_NODE, metric_type='distance')

# Виведення результатів
print("\nНайкоротші відстані та шляхи від вершини враховуючи вагу відстані:", START_NODE)
for node in sorted(path_metrics.keys(), key=int):
    print(
        f"Вершина {node}: відстань = {path_metrics[node]:.2f}, "
        f"шлях = {' -> '.join(paths_len[node])}"
    )

path_to_visualize_len = paths_len[END_VERTEX]

# Візуалізація найкоротшого шляху
visualize_path_on_weighted_graph(
    transport_graph,
    path_to_visualize_len,
    output_dir='task_03/results',
    filename='path_15_to_16_len',
    weight_type='distance'
)

#######################################################
# Виклик функції Дейкстри для часу
time_metrics, paths_time = dijkstra(transport_graph, START_NODE, metric_type='time')

# Виведення результатів
print("\nНайкоротші часи та шляхи від вершини враховуючи вагу часу:", START_NODE)
for node in sorted(time_metrics.keys(), key=int):
    print(
        f"Вершина {node}: час = {time_metrics[node]:.2f}, "
        f"шлях = {' -> '.join(paths_time[node])}"
    )

path_to_visualize_time = paths_time[END_VERTEX]

# Візуалізація найшвидшого шляху
visualize_path_on_weighted_graph(
    transport_graph,
    path_to_visualize_time,
    output_dir='task_03/results',
    filename='path_15_to_16_time',
    weight_type='time'
)

#######################################################
# Виклик функції Дейкстри для оптимізованої ваги
opt_metrics, paths_opt = dijkstra(transport_graph, START_NODE, metric_type='third_weight')

# Виведення результатів
print("\nНайкоротші відстані та шляхи від вершини враховуючи оптимізовану вагу:", START_NODE)
for node in sorted(opt_metrics.keys(), key=int):
    print(
        f"Вершина {node}: сумарна оптимізована вага = {opt_metrics[node]:.2f}, "
        f"шлях = {' -> '.join(paths_opt[node])}"
    )

path_to_visualize_opt = paths_opt[END_VERTEX]

# Візуалізація найкоротшого шляху
visualize_path_on_weighted_graph(
    transport_graph,
    path_to_visualize_opt,
    output_dir='task_03/results',
    filename='path_15_to_16_opt',
    weight_type='third_weight'
)
