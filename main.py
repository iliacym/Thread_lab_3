import os.path

import numpy as np

from task1 import Task1
from task2 import Task2
from utils.plot import Plotter as HarryPlotter
from utils.generator import Generator
from utils.config import BASE_PATH, TASK1_FILE_IN_NAME, TASK1_FILE_OUT_NAME


def main():
    print('-----------------------------')
    print('| THREAD LAB3 WELCOMES YOU! |')
    print('-----------------------------')

    while True:
        match input('Выберите задание:\n'
                    '[1] - Задача n тел\n'
                    '[2] - Решение задачи Дирихле\n'
                    '[q] - Выйти\n'):
            case '1':
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

                t1: Task1 = Task1()
                t1.read_data(f'{BASE_PATH}/{TASK1_FILE_IN_NAME}')

                result: np.ndarray = t1.run()

                with open(f'{BASE_PATH}/{TASK1_FILE_OUT_NAME}', 'w+') as file:
                    for row in result:
                        file.write(','.join(map(str, row)) + '\n')

                while True:
                    match input('Желаете ли вы проанимировать частицы? [y/n]\n'):
                        case 'y':
                            hp: HarryPlotter = HarryPlotter()
                            hp.plot()
                            break

                        case 'n':
                            break

                        case _:
                            print('Неверный ввод')

            case '2':
                pass

            case 'q':
                break

            case _:
                print('Неверный ввод')


if __name__ == '__main__':
    main()
