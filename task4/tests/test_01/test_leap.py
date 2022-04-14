import pytest
from simple_library_01.functions import is_leap


def test_not_4():
    assert is_leap(2001) == False

def test400():
    assert is_leap(2000) == True


def test_not_400_but_100():
    assert is_leap(2100) == False

def test_neg_year():
    with pytest.raises(AttributeError):
        is_leap(-1)

def test_not_100_but_4():
    assert is_leap(2004) == True



