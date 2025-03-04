from __future__ import annotations

from typing import TYPE_CHECKING, Union, Self
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
    def get(self, unit: Union[AbstractUnit, str]) -> Union[np.ndarray, int, float]:
        pass
