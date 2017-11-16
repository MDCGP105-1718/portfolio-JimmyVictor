class Fraction(object):
    def __init__(self, num, denom):
        self.num = num;
        self.denom = denom;

    def __add__(self, other):
        return (self.num + other.denom)
    def __sub__(self, other):
        return (self.num - other.denom)
    def __mul__(self, other):
        return (self.num * other.denom)
    def __div__(self, other):
        return (self.num / other.denom)
    def __inv__(self, other):
        c = self.num
        self.num = other.denom
        other.denom = c
        return Fraction(self.num, other.denom)
