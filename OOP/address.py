class Address:
    def __init__(self, postal_code: int, street: str, city: str):
        self.__street = street
        self.__city = city
        self.__postal_code = postal_code

    def set_street(self, street: str) -> None:
        self.__street = street

    def get_street(self) -> str:
        return self.__street

    def set_city(self, city: str) -> None:
        self.__city = city

    def get_city(self) -> str:
        return self.__city

    def set_postal_code(self, postal_code: int) -> None:
        self.__postal_code = postal_code

    def get_postal_code(self) -> int:
        return self.__postal_code
