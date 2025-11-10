from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousCompressibilityUnit = Literal["Pa", "MPa"]


class CompressibilityUnit(AbstractUnit):
    Pa = "1/Па"
    MPa = "1/МПа"

    def pa(self) -> bool:
        return self == self.Pa

    def mpa(self) -> bool:
        return self == self.MPa

    def coefficients(self) -> float_:
        data = {
            self.Pa: 1,
            self.MPa: 10**-6,
        }

        try:
            results = data[self]
        except KeyError:
            raise ValueError("Неизвестная еденица измерения давления")

        return results


class Compressibility(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[CompressibilityUnit, FamousCompressibilityUnit] = CompressibilityUnit.Pa,
    ) -> None:
        self.value = value

        if isinstance(unit, str):
            unit = CompressibilityUnit.from_string(unit)

        value = value * unit.coefficients()
        self.value = value

    @staticmethod
    def default_unit() -> CompressibilityUnit:
        return CompressibilityUnit.Pa

    def pa(self) -> np.ndarray:
        return self.value / CompressibilityUnit.Pa.coefficients()

    def mpa(self) -> np.ndarray:
        return self.value / CompressibilityUnit.MPa.coefficients()

    def get(self, unit: Union[CompressibilityUnit, FamousCompressibilityUnit]) -> np.ndarray:

        if isinstance(unit, str):
            unit = CompressibilityUnit.from_string(unit)

        value = self.value / unit.coefficients()
        return value
