from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_


FamousMolecularWeightUnit = Literal["g/mol"]


class MolecularWeightUnit(AbstractUnit):
    g_per_mol = "g/mol"

    def is_g_per_mol(self) -> bool:
        return self == self.g_per_mol


class MolecularWeigh(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, float_, int_],
        unit: Union[MolecularWeightUnit, MolecularWeightUnit] = MolecularWeightUnit.g_per_mol,
    ) -> None:
        if isinstance(unit, str):
            unit = MolecularWeightUnit.from_string(unit)

        if unit.is_g_per_mol():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения Массы")

        self.magnitude = magnitude

    @staticmethod
    def default_unit() -> MolecularWeightUnit:
        return MolecularWeightUnit.g_per_mol

    def g_per_mol(self) -> np.ndarray:
        return self.magnitude
