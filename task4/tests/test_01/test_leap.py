import pytest
from simple_library_01.functions import is_leap


def test_neg_year():
    with pytest.raises(AttributeError):
        is_leap(-1)


def test_400():
    assert True == is_leap(2000)


def test_not_400_but_100():
    assert False == is_leap(2100)


def test_not_100_but_4():
    assert True == is_leap(2004)


def test_not_4():
    assert False == is_leap(2001)


