import numpy as np

from task1 import Task1
from task2 import Task2
from utils.plot import Plotter as HarryPlotter
from utils.config import BASE_PATH, TASK1_FILE_OUT_NAME
from utils.surface import Surface


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
                t1: Task1 = Task1()
                t1.read_data()

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
                t2: Task2 = Task2()
                t2.read_data()

                t2.run()

                while True:
                    match input('Желаете ли построить график поверхности? [y/n]\n'):
                        case 'y':
                            surface: Surface = Surface()
                            surface.plot()
                            break

                        case 'n':
                            break

                        case _:
                            print('Неверный ввод')

            case 'q':
                break

            case _:
                print('Неверный ввод')


if __name__ == '__main__':
    main()
