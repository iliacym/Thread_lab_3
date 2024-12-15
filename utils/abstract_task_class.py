__all__ = [
    'AbstractTask'
]

from abc import ABC, abstractmethod
import numpy as np


class AbstractTask(ABC):
    @abstractmethod
    def run(self) -> np.ndarray:
        pass

    @abstractmethod
    def read_data(self, file: str):
        pass
