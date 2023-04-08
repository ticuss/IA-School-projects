import datetime


class CreatedAt:
    def __init__(self, top):
        self.created_at = datetime.datetime.now()
        self.__top = top


class DirectFlight(CreatedAt):
    def __init__(self, dep: str, arr: str, day: str, hour: int):
        self.dep = dep
        self.arr = arr
        self.day = day
        self.hour = hour
        super().__init__("top")

    def __str__(self) -> str:
        return f" Ce vol part de {self.dep} vers {self.arr} le {self.day}  à {self.hour} heure "

    @property
    def dep_arr(self):
        return self.arr + self.dep

    def dep_arr_(self):
        return self.arr + self.dep
