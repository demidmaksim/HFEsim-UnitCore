from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class TempUnit(StrEnum):
    Kelvin = "Kelvin"
    Celsius = "Celsius"
    Fahrenheit = "Fahrenheit"

    def is_kelvin(self) -> bool:
        return self == self.Kelvin

    def is_celsius(self) -> bool:
        return self == self.Celsius

    def is_fahrenheit(self) -> bool:
        return self == self.Fahrenheit


class Temperature(AbstractParam):
    __celsius_coefficient = 273.15

    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: TempUnit = TempUnit.Celsius,
    ):
        if unit.is_kelvin():
            pass
        elif unit.is_celsius():
            value = value + self.__celsius_coefficient
        elif unit.is_fahrenheit():
            value = value + self.__celsius_coefficient
            value = value - 32
            value = value / 1.8
        else:
            raise ValueError("Неизвестная еденица измерения давления")

        self.value = value

    def fahrenheit(self) -> Union[np.ndarray, int, float]:
        results = 1.8 * (self.value - self.__celsius_coefficient) + 32
        return results

    def kelvin(self) -> Union[np.ndarray, int, float]:
        return self.value
