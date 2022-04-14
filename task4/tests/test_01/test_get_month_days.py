import pytest
from simple_library_01.functions import get_month_days, is_leap


def test_1930():
    assert 30 == get_month_days(1930, 13)


def test_feb():
    assert 29 == get_month_days(2004, 2)
    assert 28 == get_month_days(2005, 2)


def test_wrong_month():
    with pytest.raises(AttributeError):
        get_month_days(2000, 69)


def test_30_days():
    assert 30 == get_month_days(2003, 6)


def test_31_days():
    assert 31 == get_month_days(2003, 5)


