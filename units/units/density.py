from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union


FamousDensityUnit = Literal["kg_per_m3", "relative", "api"]


class DensityUnit(AbstractUnit):
    kg_per_m3 = "kg_per_m3"
    relative = "relative"
    api = "api"

    def is_kg_per_m3(self) -> bool:
        return self == self.kg_per_m3

    def is_relative(self) -> bool:
        return self == self.relative

    def is_api(self) -> bool:
        return self == self.api


class Density(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, int, float],
        unit: Union[DensityUnit, FamousDensityUnit] = DensityUnit.kg_per_m3,
        relative_coefficient: Union[int, float] = 1000,
    ) -> None:
        if isinstance(unit, str):
            unit = DensityUnit.from_string(unit)

        if unit.is_kg_per_m3():
            pass
        elif unit.is_relative():
            magnitude = magnitude * relative_coefficient
        elif unit.is_api():
            magnitude = 141.5 / (magnitude + 131.5)
        else:
            raise ValueError("Неизвестная еденица измерения плотности")

        self.__relative_coefficient = relative_coefficient
        self.magnitude = magnitude

    @staticmethod
    def default_unit() -> DensityUnit:
        return DensityUnit.kg_per_m3

    def relative(self) -> Union[np.ndarray, int, float]:
        return self.magnitude / self.__relative_coefficient

    def kg_per_m3(self) -> Union[np.ndarray, int, float]:
        return self.magnitude

    def api(self) -> Union[np.ndarray, int, float]:
        return 141.5 / self.relative() - 131.5
