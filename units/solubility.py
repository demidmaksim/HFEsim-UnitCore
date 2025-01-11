from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class SolubilityUnit(StrEnum):
    SI = "м3/м3"
    Foot_per_barrel = "Foot_per_barrel"

    def is_si(self) -> bool:
        return self == self.SI

    def is_foot_per_barrel(self) -> bool:
        return self == self.Foot_per_barrel


class Solubility(AbstractParam):
    __foot_per_barrel = 0.17810760667903522

    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: SolubilityUnit = SolubilityUnit.is_si,
    ):
        if unit.is_si():
            pass
        elif unit.is_foot_per_barrel():
            value = value / self.__foot_per_barrel
        else:
            msg = "Неизвестная еденица измерения газосодержания"
            raise ValueError(msg)

        self.value = value

    def si(self) -> Union[np.ndarray, int, float]:
        return self.value

    def foot_per_barrel(self) -> Union[np.ndarray, int, float]:
        return self.value * self.__foot_per_barrel
