from __future__ import annotations

from typing import TYPE_CHECKING, Union, Self, Optional, Iterable
from enum import StrEnum
import numpy as np

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    pass


class AbstractUnit(StrEnum):

    @classmethod
    def from_string(cls, value: str) -> Self:
        for v in cls:
            if v.value == value:
                return v

        raise ValueError()


class AbstractParam(ABC):
    value: Union[np.ndarray, int, float]

    @abstractmethod
    def __init__(
        self,
        value: Union[np.ndarray, int, float],
        unit: AbstractUnit,
    ):
        pass

    @staticmethod
    @abstractmethod
    def default_unit() -> AbstractUnit:
        pass

    @abstractmethod
    def get(self, unit: Union[AbstractUnit, str]) -> Union[np.ndarray, int, float]:
        pass

    @classmethod
    def generate(
        cls,
        start: float,
        stop: float,
        step: Optional[float] = None,
        num: Optional[int] = None,
        unit: Optional[AbstractUnit] = None,
    ) -> Iterable[Self]:

        if (step is not None and num is not None) or (step is None and num is None):
            raise ValueError("необходимо задать step или num")
        elif step is not None:
            value = np.arange(start, stop, step)
        elif num is not None:
            value = np.linspace(start, stop, num=num)
        else:
            raise ValueError("Неизвестная ошибка при исполнении функции generate")

        for v in value:
            results = cls(
                value=v,
                unit=unit if unit is not unit else cls.default_unit(),
            )
            yield results
