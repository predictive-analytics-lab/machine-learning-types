"""Tests for numpy"""
from pathlib import Path
from typing import List, Sequence, TypeVar, Type

import numpy as np
import pytest

DType = TypeVar(
    "DType",
    np.bool_,
    np.complex64,
    np.complex128,
    np.float32,
    np.float64,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.str_,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
)


def assert_dtype(array: "np.ndarray[DType]", dtype: Type[DType]) -> None:
    assert array.dtype.type is dtype


# these variables are available to all other functions
a: "np.ndarray[np.float64]" = np.array([3.0, 2.0])
a = a.astype(dtype=float)
b: "np.ndarray[np.bool_]" = a == a
c: "np.ndarray[np.int64]" = np.array([[2, 3], [3, 4]])
d: "np.ndarray[np.int32]" = np.array([[1, -2], [3, 5]], dtype=np.int32)
e: "np.ndarray[np.float32]" = a.astype(np.float32)


def test_array_tuple() -> None:
    np.array((0, 1, 2))


def test_mean_std() -> None:
    f: np.ndarray[np.float32] = np.std(e, axis=0, keepdims=True)
    g: np.ndarray[np.float64] = np.std(c, axis=0, keepdims=True)
    h1: np.float64 = np.mean(c)
    i1: float = np.mean(c)
    j1: np.float32 = np.mean(e)
    k1: float = np.mean(e)
    l1: np.float64 = np.mean(b)
    # member method
    h2: np.float64 = c.mean()
    i2: float = c.mean()
    j2: np.float32 = e.mean()
    k2: float = e.mean()
    l2: np.float64 = b.mean()


def test_random_choice() -> None:
    f: int = np.random.choice(7)
    g: np.ndarray[np.int64] = np.random.choice(7, size=1)
    h: np.ndarray[np.int64] = np.random.choice(range(7), size=1)
    i: np.ndarray[np.int16] = np.random.choice(np.array([3, 7], dtype=np.int16), size=3)
    assert_dtype(i, np.int16)


def test_non_numeric() -> None:
    f: np.ndarray[np.str_] = np.array(["hello", "world"])
    g: np.ndarray[np.bool_] = np.array([True, False, True])


def test_division() -> None:
    f1: np.ndarray[np.float64] = d / c
    g1: np.ndarray[np.float32] = e / e
    h1: np.ndarray[np.float64] = e / c

    f2: np.ndarray[np.float64] = np.divide(d, c)
    g2: np.ndarray[np.float32] = np.divide(e, e)
    h2: np.ndarray[np.float64] = np.divide(e, c)
    i2: np.float64 = np.divide(60, 5)
    j2: np.ndarray[np.float64] = np.divide((60, 5, 6), 5)
    k2: np.ndarray[np.float64] = np.divide(c, 5)


def test_astype() -> None:
    f1: np.ndarray[np.float64] = e.astype(float)
    g1: np.ndarray[np.float64] = e.astype(np.float64)
    h1: np.ndarray[np.bool_] = c.astype(bool)
    i1: np.ndarray[np.int64] = d.astype(int)
    j1: np.ndarray[np.int64] = d.astype(np.int64)
    k1: np.ndarray[np.int32] = e.astype(np.int32)
    l1: np.ndarray[np.str_] = c.astype(str)

    f2: np.ndarray[np.float64] = np.asarray(e, float)
    g2: np.ndarray[np.float64] = np.asarray(e, np.float64)
    h2: np.ndarray[np.bool_] = np.asarray(c, bool)
    i2: np.ndarray[np.int64] = np.asarray(d, int)
    j2: np.ndarray[np.int64] = np.asarray(d, np.int64)
    k2: np.ndarray[np.int32] = np.asarray(e, np.int32)
    l2: np.ndarray[np.str_] = np.asarray(c, str)


def test_tolist() -> None:
    # tolist() actually returns a list, but we have to type it as Sequence because they're covariant
    f: Sequence[int] = c.tolist()
    g: Sequence[float] = e.tolist()


def test_reducing_funcs() -> None:
    """The behavior of these functions depends on whether an axis is specified"""
    sum1: np.int32 = np.sum(d)
    sum2: np.int32 = np.sum(d, axis=None)
    sum3: np.ndarray[np.int32] = np.sum(d, axis=0)

    max1: np.int32 = np.max(d)
    max2: np.int32 = np.max(d, axis=None)
    max3: np.ndarray[np.int32] = np.max(d, axis=0)

    min1: np.int32 = np.min(d)
    min2: np.int32 = np.min(d, axis=None)
    min3: np.ndarray[np.int32] = np.min(d, axis=0)

    prod1: np.int32 = np.prod(d)
    prod2: np.int32 = np.prod(d, axis=None)
    prod3: np.ndarray[np.int32] = np.prod(d, axis=0)


def test_repeat() -> None:
    f: np.ndarray[np.int16] = np.repeat(np.int16(5), 3)
    g: np.ndarray[np.int64] = np.repeat(5, 3)


def test_concatenate() -> None:
    d2: np.ndarray[np.int32] = np.concatenate([d, d], axis=1)
    d3: np.ndarray[np.int32] = np.concatenate((d, d), axis=0)
    scalar: np.float32 = np.float32(3.0)
    assert isinstance(scalar, np.float32)


def test_at_least_2d() -> None:
    arr: np.ndarray[np.float64] = np.atleast_2d(3.0)
    assert isinstance(arr, np.ndarray)
    assert_dtype(arr, np.float64)

    a: List[np.ndarray[np.int64]] = np.atleast_2d(1, [1, 2], [[1, 2]], 1)
    assert isinstance(a, list)


def test_where() -> None:
    f: np.ndarray[np.int64] = np.where(c == 2, c, d)
    g: np.ndarray[np.int64] = np.where(True, c, d)
    h1: np.ndarray[np.int64] = np.where(True, 2, 3)
    h2: np.ndarray[np.float64] = np.where(True, 2.0, 3)
    i: np.ndarray[np.int64] = np.where(c == 2, c, 3)
    j: np.ndarray[np.int32] = np.where(c == 2, 2, d)


def test_dtype() -> None:
    f: np.dtype[np.int16] = np.dtype(np.int16)
    g: np.dtype[np.int32] = np.dtype("int32")
    assert issubclass(f.type, np.integer)
    assert issubclass(g.type, np.integer)
    h: np.int16 = np.int16(3)
    assert isinstance(h.dtype, np.dtype)
    assert h.dtype.type is np.int16


def test_unsigned() -> None:
    x: np.ndarray[np.uint8] = np.array([3, 4], dtype=np.uint8)
    y: np.ndarray[np.uint8] = x + x
    z: np.ndarray[np.int32] = y


def test_addition() -> None:
    f: np.ndarray[np.float64] = d.astype(np.float64)
    g: np.ndarray[np.float64] = d + f
    assert_dtype(g, np.float64)
    h: np.ndarray[np.int8] = d.astype(np.int8)
    i: np.ndarray[np.float16] = d.astype(np.float16)
    j: np.ndarray[np.float16] = h + i
    assert_dtype(j, np.float16)


def test_finfo() -> None:
    finfo32 = np.finfo(np.float32)
    resolution: np.float32 = finfo32.resolution
    finfo64 = np.finfo(6.0)
    res64: np.float64 = finfo64.resolution


def test_cos() -> None:
    np.cos(45)
    np.cos([45, 135])


def test_deg2rad() -> None:
    np.deg2rad(45)
    np.deg2rad([45, 135])


def test_setdiff1d() -> None:
    np.setdiff1d(["A", "B"], ["B", "C"])
    np.setdiff1d([1, 2], [3, 4])
    np.setdiff1d([1.0, 2.0], [1.0, 3.0])


def test_sin() -> None:
    np.sin(45)
    np.sin([45, 135])


def test_tan() -> None:
    np.tan(45)
    np.tan([45, 135])


def test_save_load_path(tmp_path: Path) -> None:
    f = tmp_path / "foo.npy"
    np.save(f, a)
    loaded = np.load(f)
    assert loaded == pytest.approx(a)


def test_save_load_str(tmp_path: Path) -> None:
    f = str(tmp_path / "foo.npy")
    np.save(f, a)
    loaded = np.load(f)
    assert loaded == pytest.approx(a)


def test_save_load_bytes_io() -> None:
    from io import BytesIO

    f = BytesIO()
    np.save(f, a)
    f.seek(0)
    loaded = np.load(f)
    assert loaded == pytest.approx(a)


def test_rng() -> None:
    rng = np.random.default_rng(0)
    samples = rng.normal(0, 1, 200)
    more_samples = rng.normal(0, 1, 200)
    with pytest.raises(AssertionError):
        np.testing.assert_array_equal(samples, more_samples)

    rng2 = np.random.default_rng(0)
    samples2 = rng2.normal(0, 1, 200)
    np.testing.assert_array_equal(samples, samples2)


def test_interp() -> None:
    assert np.interp([0.5], [0.0, 1.0], [0.0, 100.0]) == pytest.approx([50.0])
    assert np.interp(
        [1.5], [0.0, 1.0], [0.0, 100.0], left=-1.0, right=999.0, period=None
    ) == pytest.approx([999.0])


def test_genfromtxt() -> None:
    result = np.genfromtxt(["0.1, 0.2"], dtype=np.float64, delimiter=",")
    assert list(result) == [0.1, 0.2]


def test_isfinite_isinf_isnan() -> None:
    import math

    assert np.isfinite(0.0)
    assert not np.isfinite(np.inf)
    assert np.isinf(np.inf)
    assert not np.isfinite(math.inf)
    assert not np.isfinite(np.nan)
    assert np.isnan(np.nan)
    assert np.all(np.isfinite([0.0, -np.inf]) == [True, False])
    assert np.all(np.isfinite(np.array([0.0, np.nan])) == np.array([True, False]))
    assert np.all(
        np.isfinite(np.array([np.inf, np.nan], dtype=np.float32)) == np.array([False, False])
    )
    assert np.all(np.isnan([0.0, -np.inf]) == [False, False])
    assert np.all(np.isinf([0.0, -np.inf]) == [False, True])


def test_diagonal() -> None:
    assert np.all(np.diagonal([[1]]) == np.array([1]))
    x = np.arange(12).reshape(3, 4)
    assert np.all(np.diagonal(x) == np.array([0.0, 5.0, 10.0]))


def test_allclose() -> None:
    assert np.allclose([1.0, 2.0], [1.0 + 1e-9, 2.0 + 1e-9])
    assert np.allclose(np.array([1.0, 2.0]), np.array([1.0 + 1e-9, 2.0 + 1e-9]))
    assert np.allclose(np.array([1.0, 1.0]), 1.0 + 1e-9)
    assert np.allclose(1.0 + 1e-9, np.array([1.0, 1.0]))


def test_isscalar() -> None:
    assert np.isscalar(1.0)
    assert not np.isscalar([1.0])
    assert not np.isscalar(np.array([1.0]))
    assert not np.isscalar(np.array([]))
    assert np.isscalar(np.array([1.0], dtype=np.float32)[0])


def test_newaxis() -> None:
    x = np.array([1.0, 2.0])
    assert x[np.newaxis, :].shape == (1, 2)


def test_sum_scalar_before() -> None:
    x: np.ndarray[np.float64] = 273.15 + np.array([10, 20])
    assert isinstance(x, np.ndarray)
    assert_dtype(x, np.float64)

    y: np.ndarray[np.complex128] = 10.0 + np.array([1j, 2j])
    assert isinstance(y, np.ndarray)
    assert_dtype(y, np.complex128)
