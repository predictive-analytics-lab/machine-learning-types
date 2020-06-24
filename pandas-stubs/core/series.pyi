from pathlib import Path
from typing import (
    List,
    Set,
    Tuple,
    Type,
    Union,
    overload,
    Optional,
    Dict,
    TypeVar,
    Iterator,
    Generic,
    Sequence,
    Callable,
    Any,
)
from typing_extensions import Literal
import numpy as _np

from .indexing import _LocIndexerSeries, _iLocIndexerSeries, _AtIndexerSeries
from .frame import DataFrame, _AxisType
from .indexes import Index
from .strings import StringMethods

_str = str  # needed because Series has a property called "str"...

_DType = TypeVar("_DType", _str, bool, int, float, object)
_ListLike = Union[_np.ndarray, List[_DType], Dict[_str, _np.ndarray]]
# dtypes for numpy
_DTypeNp = TypeVar(
    "_DTypeNp",
    _np.bool_,
    _np.int8,
    _np.int16,
    _np.int32,
    _np.int64,
    _np.float32,
    _np.float64,
    _np.str_,
)

class Series(Generic[_DType]):
    def __init__(
        self,
        data: Optional[
            Union[_ListLike[_DType], Series[_DType], Dict[int, _DType], Dict[_str, _DType]]
        ],
        index: Union[_str, int, Series] = ...,
    ): ...
    # magic methods
    def __and__(self, other: Series) -> Series: ...
    def __eq__(self, other: object) -> Series: ...  # type: ignore
    def __ge__(self, other: float) -> Series[bool]: ...
    def __gt__(self, other: float) -> Series[bool]: ...
    def __le__(self, other: float) -> Series[bool]: ...
    def __lt__(self, other: float) -> Series[bool]: ...
    def __ne__(self, other: object) -> Series: ...  # type: ignore
    def __mul__(self, other: float) -> Series[float]: ...
    @overload
    def __getitem__(self, idx: Union[List[_str], Index[int], Series, slice]) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[_str, int]) -> _DType: ...
    def __invert__(self: Series[bool]) -> Series[bool]: ...
    def __iter__(self) -> Iterator[_DType]: ...
    def __len__(self) -> int: ...
    def __truediv__(self, other: object) -> Series: ...
    def __or__(self, other: Series) -> Series[bool]: ...
    #
    # properties
    @property
    def iloc(self) -> _iLocIndexerSeries[_DType]: ...
    @property
    def index(self) -> Index: ...
    @property
    def item(self) -> _DType: ...
    @property
    def loc(self) -> _LocIndexerSeries[_DType]: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    @property
    def str(self) -> StringMethods: ...
    @property
    def values(self) -> _np.ndarray: ...
    #
    # methods
    def all(self, axis: Optional[_AxisType] = ..., bool_only: bool = ...) -> bool: ...
    def any(self, axis: Optional[_AxisType] = ..., bool_only: bool = ...) -> bool: ...
    def append(
        self,
        to_append: Union[Series, Sequence[Series]],
        ignore_index: bool = ...,
        verify_integrity: bool = ...,
    ) -> Series: ...
    def apply(
        self, func: Callable, convert_dtype: bool = ..., args: Tuple = ..., **kwargs: Any
    ) -> Series: ...
    @overload
    def astype(self, dtype: Type[int]) -> Series[int]: ...
    @overload
    def astype(self, dtype: Type[float]) -> Series[float]: ...
    @overload
    def copy(self) -> Series[_DType]: ...
    @overload
    def copy(self, deep: bool = ...) -> Series[_DType]: ...
    def corr(
        self, other: Series, method: Literal["pearson", "kendall", "spearman"] = ...
    ) -> float: ...
    def count(self) -> int: ...
    def fillna(self, value: Union[_DType, Dict, Series, DataFrame]) -> Series: ...
    def isna(self) -> Series[bool]: ...
    def isnull(self) -> Series[bool]: ...
    def isin(self, values: Union[Set, List, Tuple, Series]) -> Series[bool]: ...
    def ge(self, value: float) -> Series[bool]: ...
    def map(self, arg: Union[Callable, Mapping, Series], na_action: Optional[str] = ...) -> Series: ...
    def max(self) -> _DType: ...
    def mean(self) -> float: ...
    def median(self) -> float: ...
    def min(self) -> _DType: ...
    def mode(self) -> Series[_DType]: ...
    def notnull(self) -> Series[bool]: ...
    def nunique(self) -> int: ...
    @overload
    def replace(self, to_replace: int, value: int) -> Series: ...
    @overload
    def replace(self, to_replace: float, value: float) -> Series[_DType]: ...
    def reset_index(self, drop: bool = ...) -> Series: ...
    @overload
    def sort_values(self, inplace: Literal[True], ascending: bool = ...) -> None: ...
    @overload
    def sort_values(
        self, inplace: Optional[Literal[False]] = ..., ascending: bool = ...
    ) -> Series[_DType]: ...
    def std(self) -> float: ...
    def sum(self) -> float: ...
    def to_csv(self, filename: Union[Path, _str], index: bool = ...) -> None: ...
    def to_dict(self) -> Dict[Union[int, _str], _DType]: ...
    def to_frame(self, name: Optional[_str] = ...) -> DataFrame: ...
    @overload
    def to_numpy(self: Series[bool]) -> _np.ndarray[_np.bool_]: ...
    @overload
    def to_numpy(self: Series[int]) -> _np.ndarray[_np.int64]: ...
    @overload
    def to_numpy(self: Series[float]) -> _np.ndarray[_np.float64]: ...
    @overload
    def to_numpy(self: Series[object]) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Type[_DTypeNp]) -> _np.ndarray[_DTypeNp]: ...
    def unique(self) -> _np.ndarray: ...
    def update(self, other: Series) -> None: ...
    def value_counts(self, normalize: bool = ...) -> Series[_DType]: ...
    @property
    def at(self) -> _AtIndexerSeries[_DType]: ...

# Local Variables:
# blacken-line-length: 100
# blacken-allow-py36: t
# blacken-skip-string-normalization: t
# End:
