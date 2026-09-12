import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1596837868705199, "1596 83** **** 5199"),
])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number(123)


@pytest.mark.parametrize("number, expected", [
    (73654108430135874305, "**4305"),
    (64686473678894779589, "**9589"),
])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account(123)