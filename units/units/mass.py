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

    def is_kg(self) -> bool:
        return self == self.kg


class Mass(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[MassUnit, FamousMassUnit] = MassUnit.kg,
    ) -> None:
        if isinstance(unit, str):
            unit = MassUnit.from_string(unit)

        if unit.is_kg():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения Массы")

        self.value = value

    @staticmethod
    def default_unit() -> MassUnit:
        return MassUnit.kg

    def kg(self) -> np.ndarray:
        return self.value
