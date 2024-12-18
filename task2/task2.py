__all__ = [
    'Task2'
]

from typing import Optional

from task2.task2_lib import Task2Lib
from utils.abstract_task_class import AbstractTask
from utils.config import BASE_PATH, TASK2_FILE_OUT_NAME
from utils.time_checker import TimeChecker


class Task2(AbstractTask):
    def __init__(self):
        self._task2_lib: Task2Lib = Task2Lib()

        self._num_points: Optional[int] = None
        self._eps: Optional[float] = None
        self._temperature: Optional[float] = None
        self._std: Optional[float] = None
        self._threads: Optional[int] = None
        self._path: str = f'{BASE_PATH}/{TASK2_FILE_OUT_NAME}'

    @TimeChecker.measure_time
    def run(self):
        self._task2_lib.TASK2_run(self._num_points, self._eps, self._temperature, self._std, self._threads, self._path)

    def read_data(self):
        while True:
            try:
                print('Введи кол-во точек, точность, температуру, половину длины распределения, кол-во потоков')
                num_points, eps, temperature, std, threads = (t(value) for t, value in
                                                              zip((int, float, float, float, int), input().split()))

                if num_points <= 0 or eps <= 0 or std <= 0 or threads <= 0:
                    print('Кол-во точек, точность, половина длины распределения и кол-во потоков должны быть больше 0')
                    continue

                self._num_points: int = num_points
                self._eps: float = eps
                self._temperature: float = temperature
                self._std: float = std
                self._threads: int = threads

                break
            except ValueError:
                print('Неверный ввод')
