from etudiant import Etudiant

etudiant = Etudiant(
    "Doe", "John", 12345, [15, 18, 20], {"pays": "France", "ville": "Paris"}
)

print("Nom: ", etudiant.get_nom())
print("Prénom: ", etudiant.get_prenom())
print("Identifiant: ", etudiant.get_identifiant())
print("Notes: ", etudiant.get_notes())
print("Nationalité: ", etudiant.get_nationalité())

etudiant.set_nom("Smith")
etudiant.set_prenom("Jane")
etudiant.set_identifiant(67890)
etudiant.set_notes([16, 19, 17])
etudiant.set_nationalité({"pays": "Allemagne", "ville": "Berlin"})

print("Nom: ", etudiant.get_nom())
print("Prénom: ", etudiant.get_prenom())
print("Identifiant: ", etudiant.get_identifiant())
print("Notes: ", etudiant.get_notes())
print("Nationalité: ", etudiant.get_nationalité())


etudiant = Etudiant("John", "Doe", 123456, [10, 9, 8, 7, 6], {"pays": "USA"})

etudiant.ajouter_note(5)
etudiant.ajouter_note(4)

etudiant.afficher_note()

print("Moyenne de l'étudiant :", etudiant.afficher_moyenne())
