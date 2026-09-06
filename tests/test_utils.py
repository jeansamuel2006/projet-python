from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_transactions_valid():
    """Fichier JSON valide avec une liste."""
    fake_json = '[{"id": 1}, {"id": 2}]'
    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = load_transactions("fake_path.json")
    assert result == [{"id": 1}, {"id": 2}]


def test_load_transactions_not_found():
    """Fichier introuvable → liste vide."""
    result = load_transactions("fichier_inexistant.json")
    assert result == []


def test_load_transactions_not_a_list():
    """JSON qui n'est pas une liste → liste vide."""
    fake_json = '{"cle": "valeur"}'  # un dict, pas une liste
    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = load_transactions("fake_path.json")
    assert result == []
