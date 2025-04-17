from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousPresUnit = Literal["Bar", "Pascal", "MegaPascal", "At", "atm", "psi"]


class PresUnit(AbstractUnit):
    Bar = "Bar"
    Pa = "Pascal"
    MPa = "MegaPascal"
    At = "At"
    atm = "atm"
    psi = "psi"

    def is_bar(self) -> bool:
        return self == self.Bar

    def is_pascal(self) -> bool:
        return self == self.Pa

    def is_mega_pascal(self) -> bool:
        return self == self.MPa

    def is_at(self) -> bool:
        return self == self.At

    def is_atm(self) -> bool:
        return self == self.atm

    def is_psi(self) -> bool:
        return self == self.psi


class Pressure(AbstractParam):
    __psi_coefficient = 6894.76
    __bar_coefficient = 10**5

    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[PresUnit, FamousPresUnit] = PresUnit.atm,
    ):

        if isinstance(unit, str):
            unit = PresUnit.from_string(unit)

        if unit.is_bar():
            value = value * self.__bar_coefficient
        elif unit.is_psi():
            value = value * self.__psi_coefficient
        elif unit.is_pascal():
            pass
        elif unit.is_mega_pascal():
            value = value * 10**6
        elif unit.is_at():
            value = value * 98066.5
        elif unit.is_atm():
            value = value * 101325
        else:
            raise ValueError("Неизвестная еденица измерения давления")

        self.value = value

    @classmethod
    @property
    def normal_conditions(cls) -> Pressure:
        value = 0.1013 * 10**6
        return Pressure(value, PresUnit.Pa)

    @staticmethod
    def standard_conditions() -> Pressure:
        value = 0.1 * 10**6
        return Pressure(value, PresUnit.Pa)

    @staticmethod
    def default_unit() -> PresUnit:
        return PresUnit.Pa

    def psi(self) -> np.ndarray:
        return self.value / self.__psi_coefficient

    def bar(self) -> np.ndarray:
        return self.value / self.__bar_coefficient

    def pa(self) -> np.ndarray:
        return self.value

    def mpa(self) -> np.ndarray:
        return self.value / 10**6

    def at(self) -> np.ndarray:
        return self.value / 98066.5

    def atm(self) -> np.ndarray:
        return self.value / 101325

    def get(self, unit: Union[PresUnit, FamousPresUnit]) -> np.ndarray:

        if isinstance(unit, str):
            unit = PresUnit.from_string(unit)

        if unit.is_bar():
            return self.bar()
        elif unit.is_psi():
            return self.psi()
        elif unit.is_pascal():
            return self.pa()
        elif unit.is_mega_pascal():
            return self.mpa()
        elif unit.is_at():
            return self.at()
        elif unit.is_atm():
            return self.atm()
        else:
            raise ValueError("Неизвестная еденица измерения давления")
