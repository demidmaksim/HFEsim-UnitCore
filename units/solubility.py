from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Literal

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


FamousSolubilityUnit = Literal["м3/м3", "Foot_per_barrel"]


class SolubilityUnit(StrEnum):
    m3_per_m3 = "м3/м3"
    Foot_per_barrel = "Foot_per_barrel"

    def is_m3_per_m3(self) -> bool:
        return self == self.m3_per_m3

    def is_foot_per_barrel(self) -> bool:
        return self == self.Foot_per_barrel

    @classmethod
    def from_string(cls, value: FamousSolubilityUnit) -> SolubilityUnit:
        data = {
            "м3/м3": cls.m3_per_m3,
            "Foot_per_barrel": cls.Foot_per_barrel,
        }
        return data[value]


class Solubility(AbstractParam):
    __foot_per_barrel = 0.17810760667903522

    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: Union[SolubilityUnit, FamousSolubilityUnit] = SolubilityUnit.m3_per_m3,
    ):

        if isinstance(unit, str):
            unit = SolubilityUnit.from_string(unit)

        if unit.is_m3_per_m3():
            pass
        elif unit.is_foot_per_barrel():
            value = value / self.__foot_per_barrel
        else:
            msg = "Неизвестная еденица измерения газосодержания"
            raise ValueError(msg)

        self.value = value

    def m3_per_m3(self) -> Union[np.ndarray, int, float]:
        return self.value

    def foot_per_barrel(self) -> Union[np.ndarray, int, float]:
        return self.value * self.__foot_per_barrel
