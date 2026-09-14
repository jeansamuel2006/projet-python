import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_default(operations):
    assert len(filter_by_state(operations)) == 2


def test_filter_by_state_canceled(operations):
    assert len(filter_by_state(operations, "CANCELED")) == 1


def test_sort_by_date(operations):
    result = sort_by_date(operations)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"
