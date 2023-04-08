class IntervalError(Exception):
    def __init__(self, message="Error Borne bla bla "):
        self.message = message
        super().__init__(self.message)


class Intervalle:
    def __init__(self, borne_inf, borne_sup):
        if borne_inf < 0 and borne_sup < 0 and borne_inf > borne_sup:
            raise IntervalError
        self.borne_inf = borne_inf
        self.borne_sup = borne_sup

    def __add__(self, val2):
        return Intervalle(
            self.borne_inf + val2.borne_inf, self.borne_sup + val2.borne_sup
        )


intervalle = Intervalle(2, 4) + Intervalle(2,4)
