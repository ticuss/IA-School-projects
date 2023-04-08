class Etudiant:
    def __init__(
        self,
        nom: str = "",
        prenom: str = "",
        identifiant: int = 0,
        notes: list = [],
        nationalité: dict = {},
    ):
        self.__nom = nom
        self.__prenom = prenom
        self.__identifiant = identifiant
        self.__notes = notes if notes is not None else []
        self.__nationalité = nationalité if nationalité is not None else {}

    def set_nom(self, nom: str):
        self.__nom = nom

    def set_prenom(self, prenom: str):
        self.__prenom = prenom

    def set_identifiant(self, identifiant: int):
        self.__identifiant = identifiant

    def set_notes(self, notes: list):
        self.__notes = notes

    def set_nationalité(self, nationalité: dict):
        self.__nationalité = nationalité

    def get_nom(self) -> str:
        return self.__nom

    def get_prenom(self) -> str:
        return self.__prenom

    def get_identifiant(self) -> int:
        return self.__identifiant

    def get_notes(self) -> list:
        return self.__notes

    def get_nationalité(self) -> dict:
        return self.__nationalité

    def ajouter_note(self, note: int):
        self.__notes.append(note)

    def afficher_moyenne(self) -> float:
        return sum(self.__notes) / len(self.__notes)

    def afficher_note(self):
        print("Notes de l'étudiant :", self.__notes)
