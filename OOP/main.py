from xmlrpc.server import list_public_methods
from address import Address
from person import Person
from list_person import ListPerson

if __name__ == "__main__":
    address1 = Address(123, "123", "123")
    address2 = Address(1234, "1234", "1234")

    p1 = Person("toto", [address1], "M")
    p2 = Person("titi", [address2], "F")
    p3 = Person("hola", [address1, address2], "M")

    list_persons = ListPerson([p1, p2, p3])

    print(list_persons.find_by_name("toto"))
    print(list_persons.count_person_city("123"))
    print(list_persons.exists_postal_code(1234))
    list_persons.edit_person_name("toto", "new_name")
    print(p1.get_name())
    for person in list_persons:
        print(person)
    for address in p3:
        print(address)

    print(list_persons[0])
