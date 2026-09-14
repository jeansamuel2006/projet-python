from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import load_transactions, load_transactions_csv, load_transactions_xlsx


def test_load_transactions_valid():
    fake = '[{"id": 1}, {"id": 2}]'
    with patch("builtins.open", mock_open(read_data=fake)):
        assert load_transactions("x.json") == [{"id": 1}, {"id": 2}]


def test_load_transactions_not_found():
    assert load_transactions("inexistant.json") == []


@patch("src.utils.pd.read_csv")
def test_load_csv(mock_read):
    mock_read.return_value = pd.DataFrame([{"id": 1, "amount": 100}])
    assert load_transactions_csv("fake.csv") == [{"id": 1, "amount": 100}]


@patch("src.utils.pd.read_excel")
def test_load_xlsx(mock_read):
    mock_read.return_value = pd.DataFrame([{"id": 2, "amount": 200}])
    assert load_transactions_xlsx("fake.xlsx") == [{"id": 2, "amount": 200}]
