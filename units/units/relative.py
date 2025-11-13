from typing import Union

import numpy as np

from units.units.abstract import AbstractParam, AbstractUnit


class RelativeAbstractParam(AbstractParam):
    def __init__(
        self,
        magnitude: Union[np.ndarray, int, float],
        numerator: AbstractUnit,
        denominator: AbstractUnit,
    ):
        numerator_coefficients = numerator.coefficients()
        denominator_coefficients = denominator.coefficients()
        coefficients = numerator_coefficients / denominator_coefficients
        self.value = magnitude * coefficients
        self.numerator_unit = numerator
        self.denominator_unit = denominator

    @staticmethod
    def default_unit():
        raise NotImplementedError()
