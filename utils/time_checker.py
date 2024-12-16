import time


class TimeChecker:
    @staticmethod
    def measure_time(func: callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            print(f'Затраченное время: {end_time - start_time} с')

            return result

        return wrapper
