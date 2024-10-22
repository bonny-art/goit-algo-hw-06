"""
Модуль для обчислення адаптованих позицій на відрізку між двома точками.
"""

from typing import Tuple
import numpy as np

def find_adjusted_positions(
    start_pos: np.ndarray,
    end_pos: np.ndarray,
    start_size: float,
    end_size: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Знаходить дві точки на відрізку між start_pos і end_pos.

    Аргументи:
        start_pos (np.ndarray): Координати початкової точки.
        end_pos (np.ndarray): Координати кінцевої точки.
        start_size (float): Відстань від початкової точки.
        end_size (float): Відстань від кінцевої точки.

    Повертає:
        Tuple[np.ndarray, np.ndarray]: Дві точки (adjusted_start_pos, adjusted_end_pos).
    """
    direction = np.array(end_pos) - np.array(start_pos)
    direction_norm = direction / np.linalg.norm(direction)

    adjusted_start_pos = np.array(start_pos) + direction_norm * start_size
    adjusted_end_pos = np.array(end_pos) - direction_norm * end_size

    return adjusted_start_pos, adjusted_end_pos
