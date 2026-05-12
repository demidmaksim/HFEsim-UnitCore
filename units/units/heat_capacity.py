from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union


FamousHeatCapacityUnit = Literal["dj_per_kg"]


class HeatCapacityUnit(AbstractUnit):
    dj_per_kg = "dj_per_kg"

    def is_dj_per_kg(self) -> bool:
        return self == self.dj_per_kg


class HeatCapacity(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, int, float],
        unit: Union[HeatCapacityUnit, FamousHeatCapacityUnit] = HeatCapacityUnit.dj_per_kg,
    ) -> None:
        if isinstance(unit, str):
            unit = HeatCapacityUnit.from_string(unit)

        if unit.is_dj_per_kg():
            pass
        else:
            raise ValueError("Неизвестная единица измерения теплоемкости")

        self.magnitude = magnitude

    @staticmethod
    def default_unit() -> HeatCapacityUnit:
        return HeatCapacityUnit.dj_per_kg

    def dj_per_kg(self) -> Union[np.ndarray, int, float]:
        return self.magnitude
