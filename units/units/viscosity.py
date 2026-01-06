from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousViscUnit = Literal["CentiPoise", "Newton_second"]


class ViscUnit(AbstractUnit):
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
        magnitude: Union[np.ndarray, float_, int_],
        unit: Union[ViscUnit, FamousViscUnit] = ViscUnit.cP,
    ) -> None:
        if isinstance(unit, str):
            unit = ViscUnit.from_string(unit)

        if unit.is_newton():
            pass
        elif unit.is_cp():
            magnitude = magnitude * self.__cp_coefficient
        else:
            raise ValueError("Неизвестная еденица измерения вязкости")

        self.magnitude = magnitude

    @staticmethod
    def default_unit() -> ViscUnit:
        return ViscUnit.Newton

    def newton(self) -> Union[np.ndarray, int, float]:
        return self.magnitude

    def cp(self) -> Union[np.ndarray, int, float]:
        return self.magnitude / self.__cp_coefficient
