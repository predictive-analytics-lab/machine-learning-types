from typing import (
    List,
    Iterator,
    Type,
    Generic,
    TypeVar,
    Iterable,
    overload,
    Tuple,
    Callable,
)
import numpy as _np

from .frame import DataFrame
from .series import Series
from .strings import StringMethods

_str = str  # needed because Index has a property called "str"...

_T = TypeVar("_T", _str, int)
_U = TypeVar("_U", _str, int)

class Index(Generic[_T]):
    # magic methods
    def __init__(self, data: Iterable[_T]): ...
    def __eq__(self, other: object) -> Series: ...  # type: ignore
    @overload
    def __getitem__(self, idx: int) -> _T: ...
    @overload
    def __getitem__(self, idx: Index[_T]) -> Index[_T]: ...
    @overload
    def __getitem__(self, idx: Series[bool]) -> _T: ...
    @overload
    def __getitem__(self, idx: Tuple[_np.ndarray[_np.int64], ...]) -> _T: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: str) -> Index[_T]: ...  # type: ignore
    #
    # properties
    @property
    def names(self) -> List[_str]: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def str(self) -> StringMethods: ...
    @overload
    def values(self: Index[_str]) -> _np.ndarray[_np.str_]: ...
    @overload
    def values(self: Index[int]) -> _np.ndarray[_np.int64]: ...
    #
    # methods
    def astype(self, dtype: Type[_U]) -> Index[_U]: ...
    def get_level_values(self, level: _str) -> Index: ...
    def map(self, fn: Callable) -> Index: ...
    def to_frame(self) -> DataFrame: ...
    def tolist(self) -> List[_T]: ...
    @overload
    def to_numpy(self: Index[_str]) -> _np.ndarray[_np.str_]: ...
    @overload
    def to_numpy(self: Index[int]) -> _np.ndarray[_np.int64]: ...
