import os

BASE_PATH = 'tmp/'
os.makedirs(BASE_PATH, exist_ok=True)

TASK1_FILE_IN_NAME = 'input'
TASK1_FILE_OUT_NAME = 'output.csv'
SEPARATOR = ' '

G = 6.6743 * 1e-11
EPS = 9

# for plot
SIZE_OF_POINTS = 100
LEFT_EDGE = -60
RIGHT_EDGE = 90
FPS = 60

# for generator
MAX_MASS = 100
