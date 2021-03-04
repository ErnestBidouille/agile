import pytest
from app import Hotel


@pytest.fixture()
def get_hotel_nom() -> str:
    return 'Mercure Test'


@pytest.fixture()
def get_hotel_prix() -> int:
    return 80


@pytest.fixture()
def get_hotel(get_hotel_nom, get_hotel_prix) -> Hotel:
    return Hotel(get_hotel_nom, get_hotel_prix)


def test_get_prix_hotel(get_hotel, get_hotel_prix):
    assert get_hotel.prix == get_hotel_prix


def test_get_nom_hotel(get_hotel, get_hotel_nom):
    assert get_hotel.nom == get_hotel_nom


def test_prix_total(get_hotel, get_hotel_prix):
    nb_personnes_test = 5
    assert get_hotel.prix_total(
        nb_personnes_test) == get_hotel_prix * nb_personnes_test
