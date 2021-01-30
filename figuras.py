from abc import ABC, abstractmethod
from math import sqrt, pi


# Clase abstracta
class FiguraGeometrica(ABC):

    @abstractmethod
    def get_perimetro(self):  # Metodo abstracto
        pass

    @abstractmethod
    def get_area(self):  # Metodo abstracto
        pass

    @abstractmethod
    def definir_datos(self):  # Metodo abstracto
        pass


class Cuadrado(FiguraGeometrica):

    def __init__(self):  # Constructor
        self.lado = 0

    def get_perimetro(self):  # Implementacion del metodo abstracto
        # super().getPerimetro()
        return round(4 * self.lado, 2)

    def get_area(self):  # Implementacion del metodo abstracto
        # super().getArea()
        return round(self.lado * self.lado, 2)

    def definir_datos(self):  # Implementacion del metodo abstracto
        try:
            self.lado = float(input('Ingrese el lado: '))
        except Exception:
            print('Error en la entrada de datos')


class Rectangulo(FiguraGeometrica):

    def __init__(self):  # Constructor
        self.base = 0
        self.altura = 0

    def get_perimetro(self):  # Implementacion del metodo abstracto
        return round(2 * self.base + 2 * self.altura, 2)

    def get_area(self):  # Implementacion del metodo abstracto
        return round(self.base * self.altura, 2)

    def definir_datos(self):  # Implementacion del metodo abstracto
        try:
            self.base = float(input('Ingrese la base: '))
            self.altura = float(input('Ingrese la altura: '))
        except Exception:
            print('Error en la entrada de datos')


class Triangulo(FiguraGeometrica):

    def __init__(self):  # Constructor
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0

    def get_perimetro(self):  # Implementacion del metodo abstracto
        if self.ladoA > 0 and self.ladoB > 0 and self.ladoC > 0:
            return round(self.ladoA + self.ladoB + self.ladoC, 2)
        else:
            return 0

    def get_area(self):  # Implementacion del metodo abstracto
        if self.ladoA > 0 and self.ladoB > 0 and self.ladoC > 0:
            s = (self.ladoA + self.ladoB + self.ladoC) / 2
            a = self.ladoA
            b = self.ladoB
            c = self.ladoC

            return round(sqrt(s*(s-a)*(s-b)*(s-c)), 2)

        else:
            return 0

    def definir_datos(self):  # Implementacion del metodo abstracto
        try:
            self.ladoA = float(input('Ingrese el lado A: '))
            self.ladoB = float(input('Ingrese el lado B: '))
            self.ladoC = float(input('Ingrese el lado C: '))
        except Exception:
            print('Error en la entrada de datos')


class Circulo(FiguraGeometrica):

    def __init__(self):  # Constructor
        self.radio = 0

    def get_perimetro(self):  # Implementacion del metodo abstracto
        return round(2*pi*self.radio, 2)

    def get_area(self):  # Implementacion del metodo abstracto
        return round(pi * self.radio**2, 2)

    def definir_datos(self):  # Implementacion del metodo abstracto
        try:
            self.radio = float(input('Ingrese el radio: '))
        except ValueError:
            print('Error en la entrada de datos: ', ValueError.message)
