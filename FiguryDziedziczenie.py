import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""

    #  raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
    #   raise NotImplementedError


f = Figura()
f.obwod()

print(f"Wartość pi:  {math.pi}")


class Kolo(Figura):
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r ** 2


f1 = Kolo(5)
print("Obwód koła: ", f1.obwod())
print("Pole koła: ", f1.pole())


class TrojkatRownoboczny(Figura):
    def __init__(self, a):
        self.a = a
        self.h = 0.5 * a * math.sqrt(3)

    def obwod(self):
        return 3 * self.a

    def pole(self):
        return (self.a ** 2 * (3 ** 1 / 2)) / 4


f2 = TrojkatRownoboczny(5)
print("Obwód trójkąta: ", f2.obwod())
print("Pole trójkąta: ", f2.pole())


class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.b


f3 = Prostokat(2, 3)
print("Obwod prostokata: ", f3.obwod())
print("Pole prostokąta: ", f3.pole())


class Kwadrat(Prostokat):
    def __init__(self, a):
        self.a = a  # dziedzyczymy po prostokącie
        self.b = a


f4 = Kwadrat(5)
print("Obwód kwadratu: ", f4.obwod())
print("Pole kwadratu: ", f4.pole())


class Rownoleglobok(Figura):
    def __init__(self, a, b, h):
        # inny sposób przypisywania zmiennych
        # trochę skraca ilość linii
        self.a, self.b, self.h = a, b, h

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.h


f5 = Rownoleglobok(2, 4, 3)
print("Pole równoległoboku: ", f5.pole())
print("Obwód równoleggłoboku: ", f5.obwod())


class TrapezProstokatny(Figura):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

        # czwarty bok (self.c) obliczamy z Pitagorasa
        d = b - a
        self.c = (h ** 2 + d ** 2) ** 0.5

    def obwod(self):
        return sum([self.a, self.b, self.c, self.h])

    def pole(self):
        return 0.5 * (self.a + self.b) * self.h


f6 = TrapezProstokatny(2, 4, 3)
print("Pole trapezu: ", f6.pole())
print("Obwód trapezu: ", f6.obwod())
