import ctypes
import sys

if sys.platform == 'win32':
    import win32api


class Task2Lib:
    def __init__(self):
        self._dll_funcs: dict[str, callable] = {}

        if sys.platform == 'win32':
            self._lib = win32api.LoadLibrary('./task2/task2_c/libs/libThread_lab_3.dll')

            task2_run_address = win32api.GetProcAddress(self._lib, 'TASK2_run')
            task2_run_type = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_double, ctypes.c_double,
                                              ctypes.c_double, ctypes.c_int, ctypes.c_char_p)

            self._dll_funcs['TASK2_run'] = task2_run_type(task2_run_address)
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            self._lib = ctypes.CDLL('./task2/task2_c/libs/libThread_lab_3.so')

            self._dll_funcs['TASK2_run'] = self._lib.TASK2_run
        else:
            print('Анлак, братик, удачи')

    def TASK2_run(
            self,
            n_points: int,
            eps: float,
            temperature: float,
            std: float,
            threads: int,
            path: str
    ):
        self._dll_funcs['TASK2_run'](
            n_points,
            ctypes.c_double(eps),
            ctypes.c_double(temperature),
            ctypes.c_double(std),
            threads,
            path.encode('utf-8')
        )

    def __del__(self):
        if sys.platform == 'win32':
            win32api.FreeLibrary(self._lib)
