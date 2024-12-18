import numpy as np
from matplotlib import pyplot as plt

from utils.config import BASE_PATH, TASK2_FILE_OUT_NAME


class Surface:
    @staticmethod
    def plot():
        with open(f'{BASE_PATH}/{TASK2_FILE_OUT_NAME}') as file:
            mat = np.array([list(map(float, line.strip().split(' '))) for line in file])

        x, y = np.meshgrid(lin := np.linspace(0, 1, len(mat)), lin)

        _, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.plot_surface(x, y, mat, cmap='Spectral_r')
        ax.view_init(30, 35)
        plt.show()
