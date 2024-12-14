from body import Body
from Config import *
import cupy as cp


def main():
    a = cp.array([1, 2, 3, 4, 5])
    b = cp.array([6, 7, 8, 9, 10])

    c = a + b
    print(c)

    # with open(f'{BASE_PATH}/{FILE_NAME}') as file:
    #     n: int = int(file.readline())
    #     bodies: list[Body] = []
    #
    #     for line in file:
    #         bodies.append(Body(*map(float, line.split(SEPARATOR))))
    #
    # t_end: float = float(input('Введи время окончания эксперимента\n'))
    # dt: float = float(input('Введи время между шагами эксперимента\n'))


if __name__ == '__main__':
    main()
