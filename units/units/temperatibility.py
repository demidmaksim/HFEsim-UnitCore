from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousTemperatibilityUnit = Literal["1/K"]


class TemperatibilityUnit(AbstractUnit):
    Kelvin = "1/K"

    def kelvin(self) -> bool:
        return self == self.Kelvin

    def coefficients(self) -> float_:
        data = {
            self.Kelvin: 1,
        }

        try:
            results = data[self]
        except KeyError:
            raise ValueError("Неизвестная еденица измерения давления")

        return results


class Temperatibility(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, float_, int_],
        unit: Union[TemperatibilityUnit, FamousTemperatibilityUnit] = TemperatibilityUnit.Kelvin,
    ) -> None:
        self.magnitude = magnitude

        if isinstance(unit, str):
            unit = TemperatibilityUnit.from_string(unit)

        magnitude = magnitude * unit.coefficients()
        self.magnitude = magnitude

    def kelvin(self) -> np.ndarray:
        return self.magnitude / TemperatibilityUnit.Kelvin.coefficients()

    @staticmethod
    def default_unit() -> TemperatibilityUnit:
        return TemperatibilityUnit.Kelvin
