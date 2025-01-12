from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class VolumeUnit(StrEnum):
    m3 = "m3"

    def is_m3(self) -> bool:
        return self == self.m3


class Volume(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: VolumeUnit = VolumeUnit.m3,
    ) -> None:
        if unit.is_m3():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения oбъема")

        self.value = value

    def m3(self) -> Union[np.ndarray, int, float]:
        return self.value
