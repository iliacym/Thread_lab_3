__all__ = [
    'Body'
]


class Body:
    def __init__(self, mass: float, x: float, y: float, vx: float, vy: float):
        self._mass: float = mass
        self._x: float = x
        self._y: float = y
        self._vx: float = vx
        self._vy: float = vy

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float):
        self._y = y

    @property
    def vx(self) -> float:
        return self._vx

    @vx.setter
    def vx(self, vx: float):
        self._vx = vx

    @property
    def vy(self) -> float:
        return self._vy

    @vy.setter
    def vy(self, vy: float):
        self._vy = vy
