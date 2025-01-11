from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class ViscUnit(StrEnum):
    cP = "CentiPoise"
    Newton = "Newton_second"

    def is_cp(self) -> bool:
        return self == self.cP

    def is_newton(self) -> bool:
        return self == self.Newton


class Viscosity(AbstractParam):
    __cp_coefficient = 10**-3

    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: ViscUnit = ViscUnit.cP,
    ):
        if unit.is_newton():
            pass
        if unit.is_cp():
            value = value * self.__cp_coefficient
        else:
            raise ValueError("Неизвестная еденица измерения вязкости")

        self.value = value

    def cp(self) -> Union[np.ndarray, int, float]:
        return self.value / self.__cp_coefficient
