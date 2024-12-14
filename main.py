import cupy as cp
from tqdm import tqdm

from Config import *


def task1_run(body_mass: cp.ndarray, body_pos: cp.ndarray, body_vel: cp.ndarray, t_end: float, dt: float) -> cp.ndarray:
    result: cp.ndarray = cp.zeros((int(cp.ceil(t_end / dt)) + 1, body_pos.size + 1), dtype=cp.float64)
    result[:, 0] = cp.arange(0, t_end + dt, dt)
    result[0, 1:] = body_pos.flatten()

    for i in tqdm(range(int(cp.ceil(t_end / dt)))):
        v_mat: cp.ndarray = body_pos - body_pos[:, cp.newaxis, :]
        v_mat_len: cp.ndarray = cp.linalg.norm(v_mat, axis=2)
        v_mat_len[v_mat_len < EPS] = EPS
        mass_mat: cp.ndarray = cp.dot(body_mass[:, cp.newaxis], body_mass[:, cp.newaxis].T)
        f_mat: cp.ndarra = G * mass_mat[:, :, cp.newaxis] / v_mat_len[:, :, cp.newaxis] ** 3 * v_mat

        forces: cp.ndarray = cp.sum(f_mat, axis=1)
        body_pos += body_vel * dt
        body_vel += forces * dt / body_mass[:, cp.newaxis]

        result[i + 1, 1:] = body_pos.flatten()

    return result


def main():
    with open(f'{BASE_PATH}/{FILE_IN_NAME}') as file:
        n: int = int(file.readline())
        body_mass: cp.ndarray = cp.zeros(n, dtype=cp.float64)
        body_pos: cp.ndarray = cp.zeros((n, 2), dtype=cp.float64)
        body_vel: cp.ndarray = cp.zeros((n, 2), dtype=cp.float64)

        for ind, line in enumerate(file):
            buf = list(map(float, line.split(SEPARATOR)))
            body_mass[ind] = buf[0]
            body_pos[ind, 0] = buf[1]
            body_pos[ind, 1] = buf[2]
            body_vel[ind, 0] = buf[3]
            body_vel[ind, 1] = buf[4]

    t_end: float = float(input('Введи время окончания эксперимента\n'))
    dt: float = float(input('Введи время между шагами эксперимента\n'))

    result: cp.ndarray = task1_run(body_mass, body_pos, body_vel, t_end, dt).get()

    with open(f'{BASE_PATH}/{FILE_OUT_NAME}', 'w+') as file:
        for row in result:
            file.write(','.join(map(str, row)) + '\n')


if __name__ == '__main__':
    main()
