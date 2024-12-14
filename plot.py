import os
from multiprocessing import Pool, cpu_count

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


def update(frame):
    x = result[frame][::2]
    y = result[frame][1::2]
    scat.set_offsets(np.c_[x, y])
    return scat,


def process_frames(start, end):
    ani = FuncAnimation(fig, update, frames=range(start, end), interval=1000 / FPS, blit=True)
    ani.save(f"part_{start}_{end}.mp4", writer="ffmpeg", fps=FPS)


def main():
    num_processes = cpu_count()

    frames_per_process = len(result) // num_processes
    remaining_frames = len(result) % num_processes

    ranges = []
    for i in range(num_processes):
        start = i * frames_per_process
        end = (i + 1) * frames_per_process + (remaining_frames if i == num_processes - 1 else 0)
        ranges.append((start, end))

    with Pool(processes=num_processes) as pool:
        pool.starmap(process_frames, ranges)

    pool.close()
    pool.join()

    with open('file_list.txt', 'w') as f:
        for i in range(num_processes):
            f.write(f"file 'part_{ranges[i][0]}_{ranges[i][1]}.mp4'\n")

    os.system("ffmpeg -f concat -safe 0 -i file_list.txt -c copy -y -loglevel quiet animation.mp4")
    os.startfile("animation.mp4")

    for i in range(num_processes):
        os.remove(f"part_{ranges[i][0]}_{ranges[i][1]}.mp4")

    os.remove('file_list.txt')


if __name__ == '__main__':
    main()
