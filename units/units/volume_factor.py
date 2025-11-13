from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit

if TYPE_CHECKING:
    from typing import Union

    from units.utils.types_ import float_, int_

FamousVolumeFactorUnit = Literal["volume_per_volume"]


class VolumeFactorUnit(AbstractUnit):
    volume_per_volume = "volume_per_volume"

    def is_si(self) -> bool:
        return self == self.volume_per_volume


class VolumeFactor(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, float_, int_],
        unit: Union[VolumeFactorUnit, FamousVolumeFactorUnit] = VolumeFactorUnit.volume_per_volume,
    ) -> None:
        if isinstance(unit, str):
            unit = VolumeFactorUnit.from_string(unit)

        if unit.is_si():
            pass
        else:
            msg = "Неизвестная еденица измерения объемного коэфицента"
            raise ValueError(msg)

        self.value = value

    @staticmethod
    def default_unit() -> VolumeFactorUnit:
        return VolumeFactorUnit.volume_per_volume

    def volume_per_volume(self) -> np.ndarray:
        return self.value
