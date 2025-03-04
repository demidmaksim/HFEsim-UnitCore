from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union, Literal


FamousMassUnit = Literal["kg"]


class MassUnit(StrEnum):
    kg = "kg"

    def is_kg(self) -> bool:
        return self == self.kg

    @classmethod
    def from_string(cls, value: FamousMassUnit) -> MassUnit:
        data = {
            "kg": cls.kg,
        }
        return data[value]


class Mass(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: MassUnit = MassUnit.kg,
    ) -> None:

        if isinstance(unit, str):
            unit = MassUnit.from_string(unit)

        if unit.is_kg():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения Массы")

        self.value = value

    def kg(self) -> Union[np.ndarray, int, float]:
        return self.value
