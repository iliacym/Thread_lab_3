from body import Body
from Config import *
import numpy as np


# import cupy as cp

def get_force(body1: Body, body2: Body) -> np.ndarray:
    v: np.ndarray = np.array([body2.x - body1.x, body2.y - body1.y])
    return G * body1.mass * body2.mass / np.linalg.norm(v) ** 3 * v


def calc_f(bodies: list[Body]) -> list[np.ndarray]:
    f_mat: list[list[np.ndarray]] = [[np.array([0, 0])] * len(bodies) for _ in range(len(bodies))]
    for ind1, body1 in enumerate(bodies[1:]):
        for ind2, body2 in enumerate(bodies[:ind1 + 1]):
            f_mat[ind1 + 1][ind2] = get_force(body1, body2)
            f_mat[ind2][ind1 + 1] = - get_force(body1, body2)

    return [np.sum(row, axis=0) for row in f_mat]


def task1_run(bodies: list[Body], t_end: float, dt: float) -> list[list[float]]:
    result: list[list[float]] = []
    local_result: list[float] = [0]
    for body in bodies:
        local_result.append(body.x)
        local_result.append(body.y)
    result.append(local_result)
    it: int = int(np.ceil(t_end / dt))
    for i in range(it):
        forces: list[np.ndarray] = calc_f(bodies)
        local_result: list[float] = [dt * (i + 1)]
        for ind, body in enumerate(bodies):
            body.x += body.vx * dt
            body.y += body.vy * dt
            body.vx += forces[ind][0] / body.mass * dt
            body.vy += forces[ind][1] / body.mass * dt
            local_result.append(body.x)
            local_result.append(body.y)
        result.append(local_result)
    return result


def main():
    with open(f'{BASE_PATH}/{FILE_IN_NAME}') as file:
        n: int = int(file.readline())
        bodies: list[Body] = []

        for line in file:
            bodies.append(Body(*map(float, line.split(SEPARATOR))))

    t_end: float = float(input('Введи время окончания эксперимента\n'))
    dt: float = float(input('Введи время между шагами эксперимента\n'))

    result: list[list[float]] = task1_run(bodies, t_end, dt)

    with open(f'{BASE_PATH}/{FILE_OUT_NAME}', 'w+') as file:
        for row in result:
            file.write(','.join(map(str, row)) + '\n')


if __name__ == '__main__':
    main()
