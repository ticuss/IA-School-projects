from etudiant import Etudiant
from promotion import Promotion

if __name__ == "__main__":
    etudiant1 = Etudiant("John", "Doe", 1)
    etudiant1.ajouter_note(12)
    etudiant1.ajouter_note(15)
    etudiant1.ajouter_note(17)
    etudiant1.afficher_note()
    etudiant1.afficher_moyenne()

    etudiant2 = Etudiant("Jane", "Doe", 2)
    etudiant2.ajouter_note(13)
    etudiant2.ajouter_note(14)
    etudiant2.ajouter_note(16)
    etudiant2.afficher_note()
    etudiant2.afficher_moyenne()

    etudiant3 = Etudiant("Robert", "Smith", 3)
    etudiant3.ajouter_note(17)
    etudiant3.ajouter_note(19)
    etudiant3.ajouter_note(18)
    etudiant3.afficher_note()
    etudiant3.afficher_moyenne()

    etudiant4 = Etudiant("Emma", "Johnson", 4)
    etudiant4.ajouter_note(14)
    etudiant4.ajouter_note(15)
    etudiant4.ajouter_note(16)
    etudiant4.afficher_note()
    etudiant4.afficher_moyenne()

    etudiant5 = Etudiant("Michael", "Brown", 5)
    etudiant5.ajouter_note(12)
    etudiant5.ajouter_note(14)
    etudiant5.ajouter_note(13)
    etudiant5.afficher_note()
    etudiant5.afficher_moyenne()

    promotion = Promotion(
        "Promo 2022", [etudiant1, etudiant2, etudiant3, etudiant4, etudiant5]
    )
    promotion.afficher_etudiant()
    promotion.afficher_moyenne_promo()

    promotion.retirer_etudiant(5)
    promotion.afficher_etudiant()
    promotion.afficher_moyenne_promo()
    promotion.passer_examen(12)
    promotion.afficher_reussite("bla", 10)
