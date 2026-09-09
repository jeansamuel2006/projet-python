from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_valid():
    fake = '[{"id": 1}, {"id": 2}]'
    with patch("builtins.open", mock_open(read_data=fake)):
        assert load_transactions("x.json") == [{"id": 1}, {"id": 2}]


def test_load_not_found():
    assert load_transactions("inexistant.json") == []


def test_load_not_a_list():
    fake = '{"cle": "valeur"}'
    with patch("builtins.open", mock_open(read_data=fake)):
        assert load_transactions("x.json") == []
