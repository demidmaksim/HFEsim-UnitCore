from __future__ import annotations

from abc import ABC, abstractmethod
from enum import StrEnum
from typing import TYPE_CHECKING, Iterable, Iterator, Literal, Optional, Self, Union

import numpy as np

if TYPE_CHECKING:
    from units.utils.types_ import float_


class AbstractUnit(StrEnum):
    @classmethod
    def from_string(cls, value: str) -> Self:
        for v in cls:
            if v.value == value:
                return v

        raise ValueError()

    @abstractmethod
    def coefficients(self) -> float_:
        pass


class AbstractParam(Iterable, ABC):
    magnitude: np.ndarray

    @abstractmethod
    def __init__(
        self,
        magnitude: Union[np.ndarray, int, float],
        unit: AbstractUnit,
    ):
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        original_init = cls.__init__

        def new_init(
            self,
            *args,
            **kwargs,
        ):
            if len(args) > 0:
                magnitude = args[0]
            else:
                magnitude = kwargs["magnitude"]

            if not isinstance(magnitude, np.ndarray):
                magnitude = np.array([magnitude])

            if len(args) > 0:
                args = (magnitude, *args[1:])
            else:
                kwargs["magnitude"] = magnitude

            original_init(self, *args, **kwargs)

        cls.__init__ = new_init

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.magnitude.__repr__()}"

    def __iter__(self) -> Iterator[Self]:
        for v in self.magnitude:
            yield self.__class__(v, self.default_unit())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude == other.magnitude

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude != other.magnitude

    def __lt__(self, other: Self) -> np.ndarray:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude < other.magnitude

    def __gt__(self, other: Self) -> np.ndarray:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude > other.magnitude

    def __le__(self, other: Self) -> np.ndarray:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude <= other.magnitude

    def __ge__(self, other: Self) -> np.ndarray:
        if not isinstance(other, self.__class__):
            raise TypeError()

        return self.magnitude >= other.magnitude

    @staticmethod
    @abstractmethod
    def default_unit() -> AbstractUnit:
        pass

    @classmethod
    def create(
        cls,
        start: Union[float, AbstractParam],
        stop: Union[float, AbstractParam],
        step: Optional[float] = None,
        num: Optional[int] = None,
        unit: Optional[AbstractUnit] = None,
    ) -> Self:
        if unit is None:
            unit = cls.default_unit()

        if isinstance(start, AbstractParam):
            start = start.magnitude[0]
        else:
            start = cls(start, unit).magnitude[0]

        if isinstance(stop, AbstractParam):
            stop = stop.magnitude[0]
        else:
            stop = cls(stop, unit).magnitude[0]

        if (step is not None and num is not None) or (step is None and num is None):
            raise ValueError("необходимо задать step или num")
        elif step is not None:
            value = np.arange(start, stop, step)
        elif num is not None:
            value = np.linspace(start, stop, num=num)
        else:
            raise ValueError("Неизвестная ошибка при исполнении функции generate")

        return cls(magnitude=value, unit=cls.default_unit())

    @classmethod
    def generate(
        cls,
        start: Union[float, AbstractParam],
        stop: Union[float, AbstractParam],
        step: Optional[float] = None,
        num: Optional[int] = None,
        unit: Optional[AbstractUnit] = None,
    ) -> Iterable[Self]:
        if unit is None:
            unit = cls.default_unit()

        if isinstance(start, AbstractParam):
            start = start.magnitude[0]
        else:
            start = cls(start, unit).magnitude[0]

        if isinstance(stop, AbstractParam):
            stop = stop.magnitude[0]
        else:
            stop = cls(stop, unit).magnitude[0]

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
                magnitude=v,
                unit=cls.default_unit(),
            )
            yield results

    def cut(
        self,
        value: AbstractParam,
        direction: Literal["more", "less"] = "less",
        method: Literal["in", "out"] = "in",
    ) -> Self:
        if direction == "more":
            mask = self.magnitude > value.magnitude
        elif direction == "less":
            mask = self.magnitude < value.magnitude
        else:
            raise ValueError("Неизвестный direction для cut из AbstractParam")

        new_value = self.magnitude[mask]
        if method == "in" and direction == "less":
            new_value = np.concatenate((new_value, value.magnitude))
        elif method == "in" and direction == "more":
            new_value = np.concatenate((value.magnitude, new_value))
        elif method == "out":
            new_value = new_value
        else:
            raise ValueError("Неизвестный method для cut из AbstractParam")

        results = self.__class__(new_value, self.default_unit())
        return results
