from numpy import gcd
from random import randint

class GeradorChaves:

    def __init__(self):
        self.calcularNumerosPrimos()
        self.calcularN()
        self.calcularPhiN()
        self.calcularE()
        self.calcularD()
        self.mostrarResultados()

    def calcularNumerosPrimos(self):      
        numerosPrimos = []
        for c in range(2, 500):
            if all(c % i != 0 for i in range(2, c)):
                numerosPrimos.append(c)
        self.p = numerosPrimos[randint(0, len(numerosPrimos) - 1)]
        self.q = numerosPrimos[randint(0, len(numerosPrimos) - 1)]

    def calcularN(self):
        self.n = self.p * self.q

    def calcularPhiN(self):
        self.phiN = (self.p - 1) * (self.q - 1)
    
    def calcularE(self):
        self.e = []
        for i in range(1, 50000, 1):
            if gcd(i, self.phiN) == 1:
                self.e.append(i)
        self.e = self.e[randint(0, len(self.e) - 1)]
    
    def calcularD(self):
        self.d = []
        for i in range(1, 200000, 1):
            if (i * self.e) % self.phiN == 1:
                self.d.append(i)
        self.d = self.d[randint(0, len(self.d) - 1)]
    
    def mostrarResultados(self):
        print(f"Chave N: {self.n}")
        print(f"Chave E: {self.e}")
        print(f"Chave D: {self.d}")