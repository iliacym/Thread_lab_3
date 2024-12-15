__all__ = [
    'Generator'
]

import math
import random

from utils.config import BASE_PATH, TASK1_FILE_IN_NAME, LEFT_EDGE, RIGHT_EDGE, MAX_MASS


class Generator:
    def __init__(self, n: int):
        self._n: int = n

    def generate(self):
        with open(f'{BASE_PATH}/{TASK1_FILE_IN_NAME}', 'w+') as file:
            file.write(f'{self._n}\n')

            for i in range(self._n):
                file.write(f'{random.uniform(0, MAX_MASS)} '
                           f'{random.uniform(LEFT_EDGE, RIGHT_EDGE)} '
                           f'{random.uniform(LEFT_EDGE, RIGHT_EDGE)} '
                           f'{random.uniform(-math.sqrt(abs(LEFT_EDGE)), math.sqrt(abs(RIGHT_EDGE)))} '
                           f'{random.uniform(-math.sqrt(abs(LEFT_EDGE)), math.sqrt(abs(RIGHT_EDGE)))}\n')
