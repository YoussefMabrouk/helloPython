import numpy as np
import pandas as pd

def test_numpy_version():
    assert np.__version__ == "1.21.0"

def test_pandas_version():
    assert pd.__version__ == "1.3.0"
