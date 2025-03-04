from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Literal

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


FamousDensityUnit = Literal["kg_per_m3", "relative", "api"]


class DensityUnit(StrEnum):
    kg_per_m3 = "kg_per_m3"
    relative = "relative"
    api = "api"

    def is_kg_per_m3(self) -> bool:
        return self == self.kg_per_m3

    def is_relative(self) -> bool:
        return self == self.relative

    def is_api(self) -> bool:
        return self == self.api

    @classmethod
    def from_string(cls, value: FamousDensityUnit) -> DensityUnit:
        data = {
            "kg_per_m3": cls.kg_per_m3,
            "relative": cls.relative,
            "api": cls.api,
        }
        return data[value]


class Density(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: Union[DensityUnit, FamousDensityUnit] = DensityUnit.kg_per_m3,
        relative_coefficient: Union[int, float] = 1000,
    ) -> None:

        if isinstance(unit, str):
            unit = DensityUnit.from_string(unit)

        if unit.is_kg_per_m3():
            pass
        elif unit.is_relative():
            value = value * relative_coefficient
        elif unit.is_api():
            value = 141.5 / (value + 131.5)
        else:
            raise ValueError("Неизвестная еденица измерения плотности")

        self.__relative_coefficient = relative_coefficient
        self.value = value

    def relative(self) -> Union[np.ndarray, int, float]:
        return self.value / self.__relative_coefficient

    def kg_per_m3(self) -> Union[np.ndarray, int, float]:
        return self.value

    def api(self) -> Union[np.ndarray, int, float]:
        return 141.5 / self.value * 1000 - 131.5
