class Hotel:
    def __init__(self, nom: str, prix: int):
        self.nom = nom
        self.prix = prix

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        if not isinstance(nom, str) or not len(nom) > 5:
            raise ValueError('Le nom doit être une string de plus de 5 caractères')
        self.__nom = nom

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix: int):
        if not isinstance(prix, int) or prix < 0:
            raise ValueError('Le paramètre prix doit être supérieur ou égal à 0')
        self.__prix = prix

    def prix_total(self, nb_personnes : int):
        if nb_personnes < 1:
            raise ValueError('Il doit y avoir au moins une personne')
        return self.prix * nb_personnes