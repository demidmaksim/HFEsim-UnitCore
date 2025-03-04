from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Literal

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union

FamousVolumeUnit = Literal["si"]


class VolumeFactorUnit(StrEnum):
    si = "si"

    def is_si(self) -> bool:
        return self == self.si

    @classmethod
    def from_string(cls, value: FamousVolumeUnit) -> VolumeFactorUnit:
        data = {
            "si": cls.si,
        }
        return data[value]


class VolumeFactor(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: Union[VolumeFactorUnit, FamousVolumeUnit] = VolumeFactorUnit.si,
    ):

        if isinstance(unit, str):
            unit = VolumeFactorUnit.from_string(unit)

        if unit.is_si():
            pass
        else:
            msg = "Неизвестная еденица измерения объемного коэфицента"
            raise ValueError(msg)

        self.value = value

    def si(self) -> Union[np.ndarray, int, float]:
        return self.value
