import pytest
import numpy as np
import pandas as pd
import reciprocalspaceship as rs

@pytest.fixture
def na_value(dtype):
    return dtype.na_value

@pytest.fixture
def na_cmp():
    return lambda x, y: pd.isna(x) and pd.isna(y)

@pytest.fixture(params=[True, False])
def box_in_series(request):
    """Whether to box the data in a Series"""
    return request.param

@pytest.fixture(
    params=[
        lambda x: 1,
        lambda x: [1] * len(x),
        lambda x: rs.DataSeries([1] * len(x)),
        lambda x: x,
    ],
    ids=["scalar", "list", "series", "object"],
)
def groupby_apply_op(request):
    """
    Functions to test groupby.apply().
    """
    return request.param

@pytest.fixture(params=["ffill", "bfill"])
def fillna_method(request):
    """
    Parametrized fixture giving method parameters 'ffill' and 'bfill' for
    Series.fillna(method=<method>) testing.
    """
    return request.param

@pytest.fixture(params=[True, False])
def as_array(request):
    """
    Boolean fixture to support ExtensionDtype _from_sequence method testing.
    """
    return request.param

@pytest.fixture(params=[True, False])
def as_series(request):
    """
    Boolean fixture to support arr and Series(arr) comparison testing.
    """
    return request.param


@pytest.fixture(params=[True, False])
def use_numpy(request):
    """
    Boolean fixture to support comparison testing of ExtensionDtype array
    and numpy array.
    """
    return request.param

@pytest.fixture(params=[True, False])
def as_frame(request):
    """
    Boolean fixture to support Series and Series.to_frame() comparison testing.
    """
    return request.param

@pytest.fixture
def data_repeated(data):
    """
    Generate many datasets.

    Parameters
    ----------
    data : fixture implementing `data`

    Returns
    -------
    Callable[[int], Generator]:
        A callable that takes a `count` argument and
        returns a generator yielding `count` datasets.
    """

    def gen(count):
        for _ in range(count):
            yield data

    return gen

@pytest.fixture(params=["__eq__", "__ne__", "__le__", "__lt__", "__ge__", "__gt__"])
def all_compare_operators(request):
    """
    Fixture for dunder names for common compare operations
    * >=
    * >
    * ==
    * !=
    * <
    * <=
    """
    return request.param

_all_arithmetic_operators = [
    "__add__",
    "__radd__",
    "__sub__",
    "__rsub__",
    "__mul__",
    "__rmul__",
    "__floordiv__",
    "__rfloordiv__",
    "__truediv__",
    "__rtruediv__",
    "__pow__",
    "__rpow__",
    "__mod__",
    "__rmod__",
]

@pytest.fixture(params=_all_arithmetic_operators)
def all_arithmetic_operators(request):
    """
    Fixture for dunder names for common arithmetic operations.
    """
    return request.param

_all_numeric_reductions = [
    "sum",
    "max",
    "min",
    "mean",
    "prod",
    "std",
    "var",
    "median",
    "kurt",
    "skew",
]

@pytest.fixture(params=_all_numeric_reductions)
def all_numeric_reductions(request):
    """
    Fixture for numeric reduction names.
    """
    return request.param


@pytest.fixture(params=["all", "any"])
def all_boolean_reductions(request):
    """
    Fixture for boolean reduction names.
    """
    return request.param

array = {
    # Integer dtypes
    "HKL": rs.dtypes.hklindex.HKLIndexArray,
    "MTZInt": rs.dtypes.mtzint.MTZIntArray,
    "Batch": rs.dtypes.batch.BatchArray,
    "M/ISYM": rs.dtypes.m_isym.M_IsymArray,

    # Float32 dtypes
    "Intensity": rs.dtypes.intensity.IntensityArray,
    "SFAmplitude": rs.dtypes.structurefactor.StructureFactorAmplitudeArray,
    "AnomalousDifference": rs.dtypes.anomalousdifference.AnomalousDifferenceArray,
    "Stddev": rs.dtypes.stddev.StandardDeviationArray,
    "FriedelSFAmplitude": rs.dtypes.structurefactor.FriedelStructureFactorAmplitudeArray,
    "StddevFriedelSF": rs.dtypes.stddev.StandardDeviationFriedelSFArray,
    "FriedelIntensity": rs.dtypes.intensity.FriedelIntensityArray,
    "StddevFriedelI": rs.dtypes.stddev.StandardDeviationFriedelIArray,
    "NormalizedSFAmplitude": rs.dtypes.structurefactor.NormalizedStructureFactorAmplitudeArray,
    "Phase": rs.dtypes.phase.PhaseArray,
    "Weight": rs.dtypes.weight.WeightArray,
    "HendricksonLattman": rs.dtypes.phase.HendricksonLattmanArray,
    "MTZReal": rs.dtypes.mtzreal.MTZRealArray
}

@pytest.fixture
def data_int(dtype_ints):
    return array[dtype_ints[0].name]._from_sequence(np.arange(0, 100),
                                                    dtype=dtype_ints[0]())

@pytest.fixture
def data_float(dtype_floats):
    return array[dtype_floats[0].name]._from_sequence(np.arange(0, 100),
                                                      dtype=dtype_floats[0]())

@pytest.fixture
def data_all(dtype_all):
    return array[dtype_all[0].name]._from_sequence(np.arange(0, 100),
                                                   dtype=dtype_all[0]())

@pytest.fixture(params=[None, lambda x: x])
def sort_by_key(request):
    """
    Simple fixture for testing keys in sorting methods.
    Tests None (no key) and the identity key.
    """
    return request.param
