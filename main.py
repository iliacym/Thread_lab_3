import cupy as cp
from tqdm import tqdm

from Config import *


def task1_run(body_mass: cp.ndarray, body_pos: cp.ndarray, body_vel: cp.ndarray, t_end: float, dt: float) -> cp.ndarray:
    iters: int = int(cp.ceil(t_end / dt))

    result: cp.ndarray = cp.zeros((iters + 1, body_pos.size + 1), dtype=cp.float64)
    result[:, 0] = cp.arange(0, t_end + dt, dt)
    result[0, 1:] = body_pos.flatten()

    v_mat: cp.ndarray = cp.zeros((body_pos.shape[0], body_pos.shape[0], 2))
    f_mat: cp.ndarray = cp.zeros_like(v_mat)
    forces: cp.ndarray = cp.zeros_like(body_pos)

    mass_mat: cp.ndarray = cp.outer(body_mass, body_mass)
    g_mass_mat = G * mass_mat[:, :, cp.newaxis]

    body_mass = body_mass[:, cp.newaxis] * dt

    for i in tqdm(range(iters)):
        cp.subtract(body_pos, body_pos[:, cp.newaxis], out=v_mat)

        v_mat_len = cp.linalg.norm(v_mat, axis=2)
        cp.maximum(v_mat_len, EPS, out=v_mat_len)

        cp.multiply(g_mass_mat / v_mat_len[:, :, cp.newaxis] ** 3, v_mat, out=f_mat)

        cp.sum(f_mat, axis=1, out=forces)

        body_pos += body_vel * dt
        body_vel += forces / body_mass

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
