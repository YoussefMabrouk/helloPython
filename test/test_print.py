import numpy as np
import pandas as pd

def test_numpy_version():
    #assert np.__version__ == "1.25.1"
    assert int(np.__version__[0]) >= 1

def test_pandas_version():
    #assert pd.__version__ == "2.0.3"
    assert int(pd.__version__[0]) >= 1
