import pytest
from inventory import (
    calculate_total_price,
    apply_discount,
    check_stock,
)


def test_calculate_total_price():
    assert calculate_total_price(500, 3) == 1500


def test_zero_quantity():
    assert calculate_total_price(500, 0) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total_price(-100, 2)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total_price(100, -2)


def test_apply_discount():
    assert apply_discount(1000, 10) == 900


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)


def test_check_stock_available():
    assert check_stock(20, 5) is True


def test_check_stock_unavailable():
    assert check_stock(5, 10) is False
