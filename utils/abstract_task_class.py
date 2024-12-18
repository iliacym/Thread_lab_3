__all__ = [
    'AbstractTask'
]

from abc import ABC, abstractmethod


class AbstractTask(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def read_data(self):
        pass
