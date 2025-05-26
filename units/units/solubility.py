from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousSolubilityUnit = Literal["м3/м3", "Foot_per_barrel"]


class SolubilityUnit(AbstractUnit):
    m3_per_m3 = "м3/м3"
    Foot_per_barrel = "Foot_per_barrel"

    def is_m3_per_m3(self) -> bool:
        return self == self.m3_per_m3

    def is_foot_per_barrel(self) -> bool:
        return self == self.Foot_per_barrel


class Solubility(AbstractParam):
    __foot_per_barrel = 0.17810760667903522

    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[SolubilityUnit, FamousSolubilityUnit] = SolubilityUnit.m3_per_m3,
    ):
        self.value = value

        if isinstance(unit, str):
            unit = SolubilityUnit.from_string(unit)

        if unit.is_m3_per_m3():
            self.value = self.__from_m3_per_m3()
        elif unit.is_foot_per_barrel():
            self.value = self.__from_foot_per_barrel()
        else:
            msg = "Неизвестная еденица измерения газосодержания"
            raise ValueError(msg)

    def __from_m3_per_m3(self) -> np.ndarray:
        return self.value

    def __from_foot_per_barrel(self) -> np.ndarray:
        return self.value * self.__foot_per_barrel

    @staticmethod
    def default_unit() -> SolubilityUnit:
        return SolubilityUnit.m3_per_m3

    def m3_per_m3(self) -> np.ndarray:
        return self.value

    def foot_per_barrel(self) -> np.ndarray:
        return self.value / self.__foot_per_barrel

    def get(self, unit: Union[SolubilityUnit, FamousSolubilityUnit]) -> np.ndarray:

        if isinstance(unit, str):
            unit = SolubilityUnit.from_string(unit)

        if unit.is_m3_per_m3():
            return self.m3_per_m3()
        elif unit.is_foot_per_barrel():
            return self.foot_per_barrel()
        else:
            msg = "Неизвестная еденица измерения газосодержания"
            raise ValueError(msg)
