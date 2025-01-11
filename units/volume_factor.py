from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class VolumeFactorUnit(StrEnum):
    si = "si"

    def is_si(self) -> bool:
        return self == self.si


class VolumeFactor(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: VolumeFactorUnit = VolumeFactorUnit.si,
    ):
        if unit.is_si():
            pass
        else:
            msg = "Неизвестная еденица измерения объемного коэфицента"
            raise ValueError(msg)

        self.value = value

    def si(self) -> Union[np.ndarray, int, float]:
        return self.value
