from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import numpy as np

from units.abstract import AbstractParam

if TYPE_CHECKING:
    from typing import Union


class MassUnit(StrEnum):
    kg = "kg"

    def is_kg(self) -> bool:
        return self == self.kg


class Mass(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: MassUnit = MassUnit.kg,
    ) -> None:
        if unit.is_kg():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения Массы")

        self.value = value

    def kg(self) -> Union[np.ndarray, int, float]:
        return self.value
