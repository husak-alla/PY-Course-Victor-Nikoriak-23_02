import math

class Fraction:
    def __init__(self, num, den):
        if den == 0: raise ValueError("Zero denominator")
        common = math.gcd(num, den)
        self.num, self.den = num // common, den // common

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - self.den * other.num, self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __str__(self):
        return f"{self.num}/{self.den}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))