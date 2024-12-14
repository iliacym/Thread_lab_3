import math
import random

from Config import *

N = 1000

with open(f'{BASE_PATH}/{FILE_IN_NAME}', 'w+') as file:
    file.write(f'{N}\n')

    for i in range(N):
        file.write(f'{random.uniform(0, 100)} '
                   f'{random.uniform(LEFT_EDGE, RIGHT_EDGE)} '
                   f'{random.uniform(LEFT_EDGE, RIGHT_EDGE)} '
                   f'{random.uniform(-math.sqrt(abs(LEFT_EDGE)), math.sqrt(abs(RIGHT_EDGE)))} '
                   f'{random.uniform(-math.sqrt(abs(LEFT_EDGE)), math.sqrt(abs(RIGHT_EDGE)))}\n')
