from __future__ import annotations

from typing import TYPE_CHECKING, Union

import numpy as np

if TYPE_CHECKING:
    pass


class AbstractParam:
    value: Union[np.ndarray, int, float]
