from address import Address
from typing import Literal, List


class Person:
    def __init__(self, name: str, addresses: List[Address], sex: Literal["M", "F"]):
        self.__name = name
        self.__sex = sex
        self.__addresses = addresses

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

    def set_sex(self, sex: Literal["M", "F"]):
        self.__sex = sex

    def get_sex(self) -> str:
        return self.__sex

    def set_addresses(self, addresses: List[Address]):
        self.__addresses = addresses

    def get_addresses(self) -> List[Address]:
        return self.__addresses

    def __getitem__(self, i):
        return self.__addresses[i]
