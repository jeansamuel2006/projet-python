from src.search import process_bank_operations, process_bank_search


def test_process_bank_search():
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод с карты на карту"},
    ]
    result = process_bank_search(data, "Перевод")
    assert len(result) == 2


def test_process_bank_search_case_insensitive():
    data = [{"id": 1, "description": "ПЕРЕВОД организации"}]
    result = process_bank_search(data, "перевод")
    assert len(result) == 1


def test_process_bank_search_empty():
    data = [{"id": 1, "description": "Открытие вклада"}]
    result = process_bank_search(data, "несуществующее")
    assert result == []


def test_process_bank_operations():
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод организации"},
    ]
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод организации": 2, "Открытие вклада": 1}
