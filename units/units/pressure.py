from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousPresUnit = Literal["Bar", "Pascal", "MegaPascal", "At", "Atm", "psi"]


class PresUnit(AbstractUnit):
    Bar = "Bar"
    Pa = "Pascal"
    MPa = "MegaPascal"
    At = "At"
    Atm = "Atm"
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
        return self == self.Atm

    def is_psi(self) -> bool:
        return self == self.psi

    def coefficients(self) -> float_:
        data = {
            self.Bar: 10**5,
            self.Pa: 1,
            self.MPa: 10**6,
            self.At: 98066.5,
            self.Atm: 101325,
            self.psi: 6894.76,
        }

        try:
            results = data[self]
        except KeyError:
            raise ValueError("Неизвестная еденица измерения давления")

        return results


class Pressure(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, float_, int_],
        unit: Union[PresUnit, FamousPresUnit] = PresUnit.Atm,
    ) -> None:
        if isinstance(unit, str):
            unit = PresUnit.from_string(unit)

        magnitude = magnitude * unit.coefficients()
        self.magnitude = magnitude

    @classmethod
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
        return self.magnitude / PresUnit.psi.coefficients()

    def bar(self) -> np.ndarray:
        return self.magnitude / PresUnit.Bar.coefficients()

    def pa(self) -> np.ndarray:
        return self.magnitude / PresUnit.Pa.coefficients()

    def mpa(self) -> np.ndarray:
        return self.magnitude / PresUnit.MPa.coefficients()

    def at(self) -> np.ndarray:
        return self.magnitude / PresUnit.At.coefficients()

    def atm(self) -> np.ndarray:
        return self.magnitude / PresUnit.Atm.coefficients()
