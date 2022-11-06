import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного пол
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if not randomize:
            return [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]
        return [[random.randint(0, 1) for _ in range(self.cell_width)] for __ in range(self.cell_height)]

    def get_neighbours(self, cell: Cell) -> Cells:
        get = lambda a, b: self.grid[a][b]
        res = []

        y, x = cell[0], cell[1]

        if x != 0:
            res.append(get(y, x - 1))
            if y != 0:
                res.append(get(y - 1, x - 1))
            if y != self.cell_height - 1:
                res.append(get(y + 1, x - 1))
        if x != self.cell_width - 1:
            res.append(get(y, x + 1))
            if y != 0:
                res.append(get(y - 1, x + 1))
            if y != self.cell_height - 1:
                res.append(get(y + 1, x + 1))
        if y != 0:
            res.append(get(y - 1, x))
        if y != self.cell_height - 1:
            res.append(get(y + 1, x))

        return res

    def get_next_generation(self) -> Grid:
        new_grid = [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                temp = sum(self.get_neighbours((i, j)))
                if self.grid[i][j] == 1:
                    new_grid[i][j] = 1 if temp in [2, 3] else 0
                else:
                    new_grid[i][j] = 1 if temp == 3 else 0

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        pass

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
