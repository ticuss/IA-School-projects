from typing import List, Union
from person import Person


class ListPerson:
    def __init__(self, persons: List[Person]):
        self.__persons = persons

    def __getitem__(self, i) -> Person:
        return self.__persons[i]

    def __len__(self) -> int:
        return len(self.__persons)

    def set_persons(self, persons) -> None:
        self.__persons = persons

    def get_persons(self) -> List[Person]:
        return self.__persons

    def find_by_name(self, person_name: str) -> Union[Person, None]:
        for person in self.__persons:
            if person.get_name() == person_name:
                return person
            else:
                return None

    def exists_postal_code(self, pc: int) -> Union[bool, None]:
        for person in self.__persons:
            for address in person.get_addresses():
                if address.get_postal_code() == pc:
                    return True
                else:
                    continue

    def count_person_city(self, city: str) -> int:
        count = 0
        for person in self.__persons:
            for address in person.get_addresses():
                if address.get_city() == city:
                    count += 1
        return count

    def edit_person_name(self, old_name: str, new_name: str) -> None:
        for person in self.__persons:
            if person.get_name() == old_name:
                person.set_name(new_name)

    def edit_person_city(self, old_city: str, new_city: str) -> None:
        for person in self.__persons:
            for address in person.get_addresses():
                if address.get_city() == old_city:
                    address.set_city(new_city)
