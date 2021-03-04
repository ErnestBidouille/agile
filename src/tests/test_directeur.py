import pytest
from app import Directeur, Hotel


@pytest.fixture()
def get_directeur_nom() -> str:
    return 'Thomas Jefferson'


@pytest.fixture()
def get_hotel() -> Hotel:
    return Hotel("Test Mercure", 80)


@pytest.fixture()
def get_directeur_avec_hotel(get_directeur_nom, get_hotel) -> Directeur:
    return Directeur(get_directeur_nom, get_hotel)


@pytest.fixture()
def get_directeur_sans_hotel(get_directeur_nom) -> Directeur:
    return Directeur(get_directeur_nom)


def test_get_hotel_director(get_directeur_sans_hotel, get_directeur_avec_hotel,
                            get_hotel):
    assert get_directeur_avec_hotel.hotel == get_hotel
    assert get_directeur_sans_hotel.hotel == None


def test_get_nom_director(get_directeur_nom, get_directeur_sans_hotel,
                          get_directeur_avec_hotel):
    assert get_directeur_sans_hotel.nom == get_directeur_nom
    assert get_directeur_avec_hotel.nom == get_directeur_nom


def test_get_director(get_directeur_nom, get_directeur_sans_hotel):
    assert get_directeur_nom == get_directeur_sans_hotel.nom


def test_facturer_famille(get_directeur_avec_hotel, get_directeur_sans_hotel):
    assert get_directeur_avec_hotel.facturer_famille(
        5, 10) == get_directeur_avec_hotel.hotel.prix_total(5) - 10
    with pytest.raises(ValueError):
        get_directeur_sans_hotel.facturer_famille(5, 10)
    with pytest.raises(ValueError):
        get_directeur_avec_hotel.facturer_famille(5, -1)
    with pytest.raises(ValueError):
        get_directeur_avec_hotel.facturer_famille(0, 10)
