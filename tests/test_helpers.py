from pyfp.helpers import *

def test_min_arguments_helper():
    @min_arguments(3)
    def test_function(*args):
        pass

    try:
        test_function(1, 2)
        assert False
    except TypeError:
        pass

    try:
        test_function(1, 2, 3)
    except TypeError:
        assert False

    assert True