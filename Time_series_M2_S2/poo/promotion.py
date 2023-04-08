from etudiant import Etudiant


class Promotion:
    def __init__(self, nom: str = "", etudiants: list = []):
        self.nom = nom
        self.etudiants = etudiants if etudiants is not None else []

    def set_etudiants(self, etudiants: list[Etudiant]):
        self.etudiants = etudiants

    def get_etudiants(self) -> list[Etudiant]:
        return self.etudiants

    def ajouter_etudiant(self, etudiant: Etudiant):
        self.etudiants.append(etudiant)

    def retirer_etudiant(self, identifiant: int):
        for etudiant in self.etudiants:
            if etudiant.get_identifiant() == identifiant:
                self.etudiants.remove(etudiant)
                break

    def afficher_etudiant(self):
        for etudiant in self.etudiants:
            print(
                "Nom :", etudiant.get_nom(), "Identifiant :", etudiant.get_identifiant()
            )

    def afficher_moyenne_promo(self):
        moyenne_totale = 0
        nb_etudiants = len(self.etudiants)
        for etudiant in self.etudiants:
            moyenne_totale += etudiant.afficher_moyenne()
        moyenne_promo = moyenne_totale / nb_etudiants
        print("Moyenne de la promotion :", moyenne_promo)

    def passer_examen(self, note: int):
        for etudiant in self.etudiants:
            etudiant.ajouter_note(note)

    def afficher_reussite(self, matiere: str, note: float):
        print(
            f"Les étudiants ayant réussi l'examen en {matiere} avec une note de {note} ou plus sont:"
        )
        for etudiant in self.etudiants:
            moyenne = etudiant.afficher_moyenne()
            if moyenne >= note:
                print(
                    f"Nom: {etudiant.get_nom()}, identifiant: {etudiant.get_identifiant()}"
                )
