from typing import Union

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit


class RelativeAbstractParam(AbstractParam):
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        numerator: AbstractUnit,
        denominator: AbstractUnit,
    ):
        numerator_coefficients = numerator.coefficients()
        denominator_coefficients = denominator.coefficients()
        coefficients = numerator_coefficients / denominator_coefficients
        self.value = value * coefficients
        self.numerator_unit = numerator
        self.denominator_unit = denominator

    @staticmethod
    def default_unit():
        raise NotImplementedError()

    def get(self, unit: Union[AbstractUnit, str]) -> Union[np.ndarray, int, float]:
        raise NotImplementedError()
