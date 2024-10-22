"""
Модуль для обчислення нових позицій точок на відрізку з заданими відстанями від початкової та кінцевої точок.

Цей модуль містить функцію `find_adjusted_positions`, яка обчислює дві нові позиції на відрізку,
знаходячись на певній відстані від початкової та кінцевої точок.
"""

from typing import Tuple, Any
import numpy as np

def find_adjusted_positions(
    start_pos: Any,
    end_pos: Any,
    start_size: float,
    end_size: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Знаходить дві точки на відрізку між start_pos і end_pos.

    Аргументи:
        start_pos (array-like): Координати початкової точки.
        end_pos (array-like): Координати кінцевої точки.
        start_size (float): Відстань від початкової точки.
        end_size (float): Відстань від кінцевої точки.

    Повертає:
        tuple: Дві точки (adjusted_start_pos, adjusted_end_pos).
    """
    # Обчислюємо напрямок вектора
    direction = np.array(end_pos) - np.array(start_pos)
    direction_norm = direction / np.linalg.norm(direction)

    # Знаходимо нові позиції
    adjusted_start_pos = (
        np.array(start_pos) + direction_norm * start_size
    )
    adjusted_end_pos = (
        np.array(end_pos) - direction_norm * end_size
    )

    return adjusted_start_pos, adjusted_end_pos
