from typing import List
from direct_flight import DirectFlight


class Flights:
    def __init__(self, flights: List[DirectFlight]):
        self.flights = flights

    def list_succ(self, flights_dep: str):
        succ = []
        for flight in self.flights:
            if flights_dep == flight.dep:
                succ.append(flight.arr)
        return succ

    
    
    def appartient(self, city: str):
        for flight in self.flights:
            if (city == flight.dep) or (city == flight.arr):
                return f"{city}, appartient au programme de vol"

    def affiche(self):
        for flight in self.flights:
            print(flight)
