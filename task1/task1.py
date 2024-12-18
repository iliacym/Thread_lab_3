__all__ = [
    'Task1'
]

import os
import warnings

from utils.generator import Generator
from utils.time_checker import TimeChecker

warnings.filterwarnings('ignore', message='CUDA path could not be detected')

import cupy as cp

try:
    if cp.cuda.runtime.getDeviceCount() == 0:
        import numpy as cp

        print('Совместимая видеокарта не найдена, будет использован CPU')
except (cp.cuda.runtime.CUDARuntimeError, RuntimeError):
    import numpy as cp

    print('Совместимая видеокарта не найдена, будет использован CPU')

import numpy as np
from typing import Optional
from tqdm import tqdm

from utils.config import EPS, G, SEPARATOR, BASE_PATH, TASK1_FILE_IN_NAME
from utils.abstract_task_class import AbstractTask


class Task1(AbstractTask):
    def __init__(self):
        self._body_mass: Optional[cp.ndarray] = None
        self._body_pos: Optional[cp.ndarray] = None
        self._body_vel: Optional[cp.ndarray] = None
        self._t_end: Optional[float] = None
        self._dt: Optional[float] = None

    @TimeChecker.measure_time
    def run(self) -> np.ndarray:
        if self._dt is None:
            raise ValueError

        iters: int = int(cp.ceil(self._t_end / self._dt))

        result: cp.ndarray = cp.zeros((iters + 1, self._body_pos.size + 1), dtype=cp.float64)
        result[:, 0] = cp.arange(iters + 1) * self._dt
        result[0, 1:] = self._body_pos.flatten()

        v_mat: cp.ndarray = cp.zeros((len(self._body_pos), len(self._body_pos), 2), dtype=cp.float64)
        f_mat: cp.ndarray = cp.zeros_like(v_mat)
        forces: cp.ndarray = cp.zeros_like(self._body_pos)

        mass_mat: cp.ndarray = cp.outer(self._body_mass, self._body_mass)
        g_mass_mat = G * mass_mat[:, :, cp.newaxis]

        body_mass = self._body_mass[:, cp.newaxis] / self._dt

        for i in tqdm(range(iters)):
            cp.subtract(self._body_pos, self._body_pos[:, cp.newaxis], out=v_mat)

            v_mat_len = cp.linalg.norm(v_mat, axis=2)
            cp.maximum(v_mat_len, EPS, out=v_mat_len)

            cp.multiply(g_mass_mat / v_mat_len[:, :, cp.newaxis] ** 3, v_mat, out=f_mat)

            cp.sum(f_mat, axis=1, out=forces)

            self._body_pos += self._body_vel * self._dt
            self._body_vel += forces / body_mass

            result[i + 1, 1:] = self._body_pos.flatten()

        return np.array(result.get()) if type(result) is not np.ndarray else result

    def read_data(self):  # todo дописать проверку на диапазон ввода
        while True:
            match input('Желаете ли вы сгенерировать данные тел? [y/n]\n'):
                case 'y':
                    while True:
                        try:
                            n: int = int(input('Введите количество тел\n'))
                            break
                        except ValueError:
                            print('Неверный ввод')

                    generator: Generator = Generator(n)
                    generator.generate()

                    break

                case 'n':
                    if not os.path.exists(f'{BASE_PATH}/{TASK1_FILE_IN_NAME}'):
                        print('Файл не найден')
                        continue

                    break
                case _:
                    print('Неверный ввод')

        with open(f'{BASE_PATH}/{TASK1_FILE_IN_NAME}') as file:
            n: int = int(file.readline())
            self._body_mass: cp.ndarray = cp.zeros(n, dtype=cp.float64)
            self._body_pos: cp.ndarray = cp.zeros((n, 2), dtype=cp.float64)
            self._body_vel: cp.ndarray = cp.zeros_like(self._body_pos)

            for ind, line in enumerate(file):
                buf = list(map(float, line.split(SEPARATOR)))
                self._body_mass[ind] = buf[0]
                self._body_pos[ind, 0] = buf[1]
                self._body_pos[ind, 1] = buf[2]
                self._body_vel[ind, 0] = buf[3]
                self._body_vel[ind, 1] = buf[4]

        while True:
            try:
                self._t_end: float = float(input('Введи время окончания эксперимента (в секундах)\n'))
                break
            except ValueError:
                print('Неверный ввод')

        while True:
            try:
                self._dt: float = float(input('Введи время между шагами эксперимента (в секундах)\n'))
                break
            except ValueError:
                print('Неверный ввод')
