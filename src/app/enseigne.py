from .hotel import Hotel
from typing import Iterable


class Enseigne:
    def __init__(self, nom: str, hotels: Iterable[Hotel]) -> None:
        self.nom = nom
        self.__hotels = set()
        for hotel in hotels:
            if hotel and not isinstance(hotel, Hotel):
                self.__hotels = dict()
                raise ValueError('Le parametre hotel doit être une liste d\'hotels')
            self.__hotels.add(hotel)

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        if not isinstance(nom, str):
            raise ValueError('Le nom de l\'enseigne doit être une string')
        self.__nom = nom

    @property
    def hotels(self):
        return self.__hotels
      
