from direct_flight import DirectFlight
from flights import Flights


f1 = DirectFlight("Paris", "Marseille", "Lundi", 8)
f2 = DirectFlight("Paris", "Dijon", "Lundi", 8)
f3 = DirectFlight("Paris", "Lyon", "Lundi", 8)
f4 = DirectFlight("Hehe", "Haha", "Lundi", 8)

flights = Flights(flights=[f1, f2, f3, f4])

print(20 * "#", "Liste des vols", 20 * "#")
flights.affiche()
print(20 * "#", "Liste des villes d'arrivée", 20 * "#")
print(flights.list_succ("Paris"))
print(20 * "#", "Liste des vols en partance de Paris", 20 * "#")
print(flights.appartient("Paris"))
