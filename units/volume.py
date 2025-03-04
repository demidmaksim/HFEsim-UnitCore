from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Literal

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


FamousVolumeUnit = Literal["m3"]


class VolumeUnit(StrEnum):
    m3 = "m3"

    def is_m3(self) -> bool:
        return self == self.m3

    @classmethod
    def from_string(cls, value: FamousVolumeUnit) -> VolumeUnit:
        data = {
            "m3": cls.m3,
        }
        return data[value]


class Volume(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: Union[VolumeUnit, FamousVolumeUnit] = VolumeUnit.m3,
    ) -> None:

        if isinstance(unit, str):
            unit = VolumeUnit.from_string(unit)

        if unit.is_m3():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения oбъема")

        self.value = value

    def m3(self) -> Union[np.ndarray, int, float]:
        return self.value
