from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousMassUnit = Literal["kg"]


class MassUnit(AbstractUnit):
    kg = "kg"
    ton = "ton"

    def is_kg(self) -> bool:
        return self == self.kg

    def is_ton(self) -> bool:
        return self == self.ton


class Mass(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, float_, int_],
        unit: Union[MassUnit, FamousMassUnit] = MassUnit.kg,
    ) -> None:
        if isinstance(unit, str):
            unit = MassUnit.from_string(unit)

        if unit.is_kg():
            pass
        elif unit.is_ton():
            magnitude = magnitude * 1000
        else:
            raise ValueError("Неизвестная еденица измерения Массы")

        self.magnitude = magnitude

    @staticmethod
    def default_unit() -> MassUnit:
        return MassUnit.kg

    def kg(self) -> np.ndarray:
        return self.magnitude

    def ton(self) -> np.ndarray:
        return self.magnitude / 1000
