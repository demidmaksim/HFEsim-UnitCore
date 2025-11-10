from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousTempUnit = Literal["Kelvin", "Celsius", "Fahrenheit", "Rankin"]


class TempUnit(AbstractUnit):
    Kelvin = "Kelvin"
    Celsius = "Celsius"
    Fahrenheit = "Fahrenheit"
    Rankin = "Rankin"

    def is_kelvin(self) -> bool:
        return self == self.Kelvin

    def is_celsius(self) -> bool:
        return self == self.Celsius

    def is_fahrenheit(self) -> bool:
        return self == self.Fahrenheit

    def is_rankin(self) -> bool:
        return self == self.Rankin


class Temperature(AbstractParam):
    __celsius_coefficient = 273.15

    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[TempUnit, FamousTempUnit] = TempUnit.Celsius,
    ) -> None:

        if isinstance(unit, str):
            unit = TempUnit.from_string(unit)

        if unit.is_kelvin():
            pass
        elif unit.is_celsius():
            value = value + self.__celsius_coefficient
        elif unit.is_fahrenheit():
            value = value - 32
            value = value / 1.8
            value = value + self.__celsius_coefficient
        else:
            raise ValueError("Неизвестная еденица измерения температуры")

        self.value = value

    @staticmethod
    def default_unit() -> TempUnit:
        return TempUnit.Kelvin

    def celsius(self) -> np.ndarray:
        return self.value - self.__celsius_coefficient

    def fahrenheit(self) -> np.ndarray:
        results = 1.8 * (self.value - self.__celsius_coefficient) + 32
        return results

    def kelvin(self) -> np.ndarray:
        return self.value

    def rankin(self) -> np.ndarray:
        return self.fahrenheit() + 459.67

    def get(self, unit: Union[TempUnit, FamousTempUnit]) -> np.ndarray:

        if isinstance(unit, str):
            unit = TempUnit.from_string(unit)

        if unit.is_kelvin():
            return self.kelvin()
        elif unit.is_celsius():
            return self.celsius()
        elif unit.is_fahrenheit():
            return self.fahrenheit()
        elif unit.is_rankin():
            return self.rankin()
        else:
            raise ValueError("Неизвестная единица измерения температуры")
