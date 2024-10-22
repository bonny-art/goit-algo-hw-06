"""
Модуль для реалізації алгоритмів пошуку шляху в графі станцій.
Включає реалізації пошуку в глибину (DFS) та пошуку в ширину (BFS).
"""

from collections import deque
import networkx as nx

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
