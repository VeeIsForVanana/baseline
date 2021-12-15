from fighter import Fighter

from equippable import Equippable
from base_component import BaseComponent

class Attribute():
    """General class for all attributes (numerical stats with maxima and minima attached to entity components)"""
    parent: BaseComponent

    def __init__(self, current: int, max: int, min: int = 0):
        self._current = current
        self._max = max
        self._min = min

    @property
    def value(self) -> int:
        return self._current

    def new_value(self, new_value: int) -> None:
        self._current = min(self._max, max(self._min, new_value))

    def add_to_value(self, amount: int):
        self.new_value(self._current + amount)

    @property
    def max(self) -> int:
        return self._max

    @max.setter
    def max(self, new_max: int) -> None:
        self._max = max(self.value, new_max)

    @property
    def min(self) -> int:
        return self._min

    @min.setter
    def min(self, new_min: int) -> None:
        self._min = min(self.value, new_min)


class HealthAttribute(Attribute):

    parent: Fighter

    name = "HP"

    def __init__(self, current: int, max: int = 20):
        super().__init__(current, max)

class DefenseAttribute(Attribute):

    parent: BaseComponent

    name = ("Defense" if not isinstance(parent, Equippable) else "Defense Bonus")

class PowerAttribute(Attribute):

    parent: BaseComponent

    name = ("Attack" if not isinstance(parent, Equippable) else "Attack Bonus")
