from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousVolumeUnit = Literal["m3"]


class VolumeUnit(AbstractUnit):
    m3 = "m3"

    def is_m3(self) -> bool:
        return self == self.m3


class Volume(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[VolumeUnit, FamousVolumeUnit] = VolumeUnit.m3,
    ) -> None:

        if isinstance(unit, str):
            unit = VolumeUnit.from_string(unit)

        if unit.is_m3():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения oбъема")

        self.value = value

    @staticmethod
    def default_unit() -> VolumeUnit:
        return VolumeUnit.m3

    def m3(self) -> np.ndarray:
        return self.value

    def get(self, unit: Union[VolumeUnit, FamousVolumeUnit]) -> np.ndarray:

        if isinstance(unit, str):
            unit = VolumeUnit.from_string(unit)

        if unit.is_m3():
            return self.m3()
        else:
            raise ValueError("Неизвестная еденица измерения oбъема")
