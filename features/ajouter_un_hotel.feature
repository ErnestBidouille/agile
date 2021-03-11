Feature: US_001 Ajouter un hôtel à une enseigne

    Scenario: Ajouter un hotel à une enseigne
        Given Une enseigne et un hotel
        When On ajoute à l'enseigne l'hôtel
        Then L'hotel est dans la liste des hôtels
        And L'hotel a pour enseigne l'enseigne
