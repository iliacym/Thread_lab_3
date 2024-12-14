import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Config import *

result = []
with open(f'{BASE_PATH}/{FILE_OUT_NAME}') as file:
    for row in file:
        result.append(list(map(float, row.strip().split(',')))[1:])

result = np.array(result)
fig, ax = plt.subplots()

scat = ax.scatter([], [], s=SIZE_OF_POINTS)
ax.set_xlim(LEFT_EDGE, RIGHT_EDGE)
ax.set_ylim(LEFT_EDGE, RIGHT_EDGE)


# Функция для обновления данных на каждом кадре
def update(frame):
    x = result[frame][::2]
    y = result[frame][1::2]

    scat.set_offsets(np.c_[x, y])
    return scat,


ani = FuncAnimation(fig, update, frames=len(result), interval=TIME_DELAY, blit=True)

ani.save("animation.mp4", writer="ffmpeg", fps=1000 // TIME_DELAY)
