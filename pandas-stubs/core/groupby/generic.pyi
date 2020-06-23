from typing import overload, Optional, Union, List, Dict, Iterator
import numpy as _np

from pandas.core.frame import DataFrame
from pandas.core.series import Series
from ..frame import _FunctionLike

_str = str  # needed because Series has a property called "str"...

class GroupBy: ...

class DataFrameGroupBy(GroupBy):
    @overload
    def __getitem__(self, item: _str) -> SeriesGroupBy: ...
    @overload
    def __getitem__(self, item: List[_str]) -> DataFrameGroupBy: ...
    def __getattr__(self, name: _str) -> SeriesGroupBy: ...
    def __iter__(self) -> Iterator: ...
    def aggregate(
        self, func: Union[_FunctionLike, List[_FunctionLike], Dict[_str, _FunctionLike]],
    ) -> DataFrame: ...
    agg = aggregate
    def count(self) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def max(self) -> DataFrame: ...
    def mean(self) -> DataFrame: ...
    def median(self) -> DataFrame: ...
    def min(self) -> DataFrame: ...
    def nunique(self, dropna: bool = ...) -> DataFrame: ...
    def quantile(self, q: float = ..., interpolation: str = ...) -> DataFrame: ...
    def std(self, ddof: int = ...) -> DataFrame: ...
    def sum(self) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def var(self, ddof: int = ...) -> DataFrame: ...

class SeriesGroupBy(GroupBy):
    def __getitem__(self, item: _str) -> Series: ...
    def count(self) -> Series: ...
    def head(self, n: int = ...) -> Series: ...
    def max(self) -> Series: ...
    def mean(self) -> Series: ...
    def median(self) -> Series: ...
    def min(self) -> Series: ...
    def nunique(self, dropna: bool = ...) -> Series: ...
    def quantile(self, q: float = ..., interpolation: str = ...) -> Series: ...
    def std(self, ddof: int = ...) -> Series: ...
    def sum(self) -> Series: ...
    def tail(self, n: int = ...) -> Series: ...
    def unique(self) -> Series: ...
    def var(self, ddof: int = ...) -> Series: ...
