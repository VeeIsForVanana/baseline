from base_component import BaseComponent
from fighter import Fighter

class Attribute(BaseComponent):
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