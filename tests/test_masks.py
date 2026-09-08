import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number(123)


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account(123)

    @pytest.mark.parametrize(
        "number, expected",
        [
            (64686473678894779589, "**9589"),
            (35383033474447895560, "**5560"),
            (73654108430135874305, "**4305"),
        ],
    )
    def test_mask_account_parametrized(number, expected):
        assert get_mask_account(number) == expected

        @pytest.mark.parametrize(
            "number, expected",
            [
                (7000792289606361, "7000 79** **** 6361"),
                (1596837868705199, "1596 83** **** 5199"),
                (7158300734726758, "7158 30** **** 6758"),
            ],
        )
        def test_mask_card_parametrized(number, expected):
            assert get_mask_card_number(number) == expected
