__all__ = [
    'AbstractTask'
]

from abc import ABC, abstractmethod
import numpy as np


class AbstractTask(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def read_data(self):
        pass
