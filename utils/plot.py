__all__ = [
    'Plotter'
]

import os
import sys
import subprocess
from multiprocessing import Pool, cpu_count

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from utils.config import LEFT_EDGE, RIGHT_EDGE, FPS, SIZE_OF_POINTS, BASE_PATH, TASK1_FILE_OUT_NAME


class Plotter:
    def __init__(self):
        self._file_list: str = f'{BASE_PATH}/file_list.txt'
        self._out_file: str = f'{BASE_PATH}/animation.mp4'

        result: list[list[float]] = []
        with open(f'{BASE_PATH}/{TASK1_FILE_OUT_NAME}') as file:
            for row in file:
                result.append(list(map(float, row.strip().split(',')))[1:])

        self._result: np.ndarray = np.array(result)
        self._fig, ax = plt.subplots()

        ax.axis('off')

        self._scat = ax.scatter([], [], s=SIZE_OF_POINTS)
        ax.set_xlim(LEFT_EDGE, RIGHT_EDGE)
        ax.set_ylim(LEFT_EDGE, RIGHT_EDGE)

    def _update(self, frame):
        x = self._result[frame][::2]
        y = self._result[frame][1::2]
        self._scat.set_offsets(np.c_[x, y])
        return self._scat,

    def _process_frames(self, start, end):
        ani = FuncAnimation(self._fig, self._update, frames=range(start, end), interval=1000 / FPS, blit=True)
        ani.save(f'{BASE_PATH}/part_{start}_{end}.mp4', writer='ffmpeg', fps=FPS)

    def plot(self):
        num_processes = cpu_count()

        frames_per_process = len(self._result) // num_processes
        remaining_frames = len(self._result) % num_processes

        ranges = []
        for i in range(num_processes):
            start = i * frames_per_process
            end = (i + 1) * frames_per_process + (remaining_frames if i == num_processes - 1 else 0)
            ranges.append((start, end))

        try:
            subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print('Броу, установи ffmpeg, это бесплатно')
            return
        except subprocess.CalledProcessError:
            print('Броу, переустанови ffmpeg, твой не работает')
            return

        with Pool(processes=num_processes) as pool:
            pool.starmap(self._process_frames, ranges)

        pool.close()
        pool.join()

        with open(self._file_list, 'w') as f:
            for i in range(num_processes):
                f.write(f"file 'part_{ranges[i][0]}_{ranges[i][1]}.mp4'\n")

        os.system(f'ffmpeg -f concat -safe 0 -i {self._file_list} -c copy '
                  f'-y -loglevel quiet {self._out_file}')

        if sys.platform == 'win32':
            subprocess.run(['start', self._out_file], shell=True)
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            subprocess.run(['xdg-open', self._out_file])
        else:
            print('Файл animation.mp4 сохранен в папке tmp, удачи')

        for i in range(num_processes):
            os.remove(f'{BASE_PATH}/part_{ranges[i][0]}_{ranges[i][1]}.mp4')

        os.remove(self._file_list)
