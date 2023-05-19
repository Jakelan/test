class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja_verte):
        if isinstance(nauja_verte, int):
            self.__verte = nauja_verte
        else:
            print("Netinkamas verte parametro formatas. Verte turi buti skaicius.")


namas1 = Namas("65 kvadratu", 30000)
print(namas1.verte)

namas1.verte = 50000
print(namas1.verte)

namas1.verte = "labas"
