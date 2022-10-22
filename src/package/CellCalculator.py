from calendar import c
from ctypes import cdll
from re import A
from this import d
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
from enum import Enum

from abc import ABC, abstractmethod

E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]
MIN_RES = 1e+0
MAX_RES = 1e+6
MIN_CAP = 47e-12
MAX_CAP = 470e-6

class Cell(ABC):
    def __init__(self):
        self.tf = {}
        super().__init__()

    @abstractmethod
    def calculateComponentsZPK(self, z, p, k):
        pass
    @abstractmethod
    def calculateComponentsND(self, Ncoeff, Dcoeff):
        pass
    @abstractmethod
    def transferFromComponents(self):
        pass


class SallenKey(Cell):
    def __init__(self):
        super().__init__()

    def calculateComponentsZPK(self, z, p, k):
        pass
    def calculateComponentsND(self, Ncoeff, Dcoeff):
        pass
    def transferFromComponents(self):
        pass
    def calculateLP(self):
        self.K = 3 - 1 / self.Q 
        pass
    def calculateHP(self):
        pass


class Rauch(Cell):
    def __init__(self):
        super().__init__()

    def calculateComponentsZPK(self, z, p, k):
        pass
    def calculateComponentsND(self, Ncoeff, Dcoeff):
        pass
    def transferFromComponents(self):
        pass

class Sedra(Cell):
    def __init__(self):
        self.Q0 = 1
        super().__init__()

    def calculateComponentsZPK(self, z, p, k):
        pass
    def calculateComponentsND(self, Ncoeff, Dcoeff):
        pass
    def transferFromComponents(self):
        pass

    def calculateLP(self):
        pass
    def calculateHP(self):
        pass


class FleischerTow(Cell):
    def __init__(self, C1=1e-9, C2=1e-9, R8=1e3, k1=1, k2=1):
        self.C1 = C1
        self.C2 = C2
        self.R8 = R8
        self.k1 = k1
        self.k2 = k2

    def calculateComponentsZPK(self, z, p, k):
        tftemp = signal.zpk2tf(z, p, k)
        self.calculateComponentsND(tftemp[0], tftemp[1])

    def calculateComponentsND(self, Ncoeff, Dcoeff):
        assert len(Dcoeff) >= len(Ncoeff)
        assert len(Dcoeff) < 4

        m = Ncoeff[0] / Dcoeff[0]
        c = Ncoeff[1] / Dcoeff[0]
        d = Ncoeff[2] / Dcoeff[0]
        a = Dcoeff[1] / Dcoeff[0]
        b = Dcoeff[2] / Dcoeff[0]

        self.wz = np.sqrt(d / m)
        self.wp = np.sqrt(b)
        self.Q = np.sqrt(b) / a

        self.R1 = 1 / (a * self.C1)
        self.R2 = self.k1 / (np.sqrt(b) * self.C2)
        self.R3 = 1 / (self.k1 * self.k2 * np.sqrt(b) * self.C1)
        self.R4 = 1 / (self.k2 * (m * a - c) * self.C1)
        self.R5 = self.k1 * np.sqrt(b) / (d * self.C2)
        self.R6 = self.R8 / m
        self.R7 = self.k2 * self.R8

        self.resistors = [0, self.R1, self.R2, self.R3, self.R4, self.R5, self.R6, self.R7, self.R8]
        self.capacitors = [0, self.C1, self.C2]

    def transferFromComponents(self):
        m = self.R8 / self.R6
        c = (self.R8 / (self.R1 * self.C1)) * (1 / self.R6 - self.R1 / (self.R4 * self.R7))
        d = self.R8 / (self.R3 * self.R5 * self.R7 * self.C1 * self.C2)
        a = 1 / (self.R1 * self.C1)
        b = self.R8 / (self.R2 * self.R3 * self.C1 * self.C2 * self.R7)

        self.tf = signal.TransferFunction([m, c, d], [1, a, b])

        
ft = FleischerTow(C1=47e-9, C2=47e-9, R8=1.5e3)

da = 1100
dp = 10e3
fo = 44.3e3
Aa = 48
Ap = 6
nMax = 2

wpMin = (-dp + np.sqrt(dp**2 + 4*fo**2))*np.pi
wpMax = (dp + np.sqrt(dp**2 + 4*fo**2))*np.pi
waMin = (-da + np.sqrt(da**2 + 4*fo**2))*np.pi
waMax = (da + np.sqrt(da**2 + 4*fo**2))*np.pi

n, Wn= signal.cheb2ord([wpMin,wpMax], [waMin,waMax], Ap, Aa, analog=True)
z, p, k = signal.cheby2(n, Aa, Wn, 'stop', analog=True, output = 'zpk')
sos = signal.cheby2(n, Aa, Wn, 'stop', analog=True, output = 'sos')

ft.calculateComponentsND(sos[0][0:3], sos[0][3:6])
print('R1:', ft.R1)
print('R2:', ft.R2)
print('R3:', ft.R3)
print('R4:', ft.R4)
print('R5:', ft.R5)
print('R6:', ft.R6)
print('R7:', ft.R7)
print('R8:', ft.R8)
print('C2:', ft.C1)
print('C1:', ft.C2)