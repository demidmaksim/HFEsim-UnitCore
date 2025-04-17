from typing import get_args

import pytest

from units.units import (
    DensityUnit,
    FamousDensityUnit,
    FamousMassUnit,
    FamousPresUnit,
    FamousSolubilityUnit,
    FamousTempUnit,
    FamousViscUnit,
    FamousVolumeFactorUnit,
    FamousVolumeUnit,
    MassUnit,
    PresUnit,
    SolubilityUnit,
    TempUnit,
    ViscUnit,
    VolumeFactorUnit,
    VolumeUnit,
)
from units.units.abstract import AbstractUnit

all_param = [
    (DensityUnit, FamousDensityUnit),
    (PresUnit, FamousPresUnit),
    (SolubilityUnit, FamousSolubilityUnit),
    (TempUnit, FamousTempUnit),
    (ViscUnit, FamousViscUnit),
    (VolumeFactorUnit, FamousVolumeFactorUnit),
    (MassUnit, FamousMassUnit),
    (VolumeUnit, FamousVolumeUnit),
]


@pytest.mark.parametrize("units, famous", all_param)
def test_famous_unit_value(unit: AbstractUnit, famous):
    famous = get_args(famous)
    for u in unit:
        assert u.value in famous

    for f in famous:
        assert f in [u.value for u in unit]


@pytest.mark.parametrize("units, famous", all_param)
def test_from_string(unit: AbstractUnit, famous):
    for f in get_args(famous):
        assert unit.from_string(f) in [u for u in unit]
        assert unit.from_string(f).value in [u.value for u in unit]
