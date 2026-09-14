from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_rub():
    transaction = {"operationAmount": {"amount": "500.00", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 500.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 7500.0}
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    assert convert_to_rub(transaction) == 7500.0
