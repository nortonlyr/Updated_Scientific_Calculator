import math

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y

    def square(self, x):
        return x ** 2

    def powerof(self, x, y):
        return x ** y

    def square_root(self, x):
        return x ** (1/2)

    def inv(self, x):
        return 1 / x

    def sinrad(self, x):
        return math.sin(x)

    def cosrad(self, x):
        return math.cos(x)

    def tanrad(self, x):
        return math.tan(x)

    def cotrad(self, x):
        return 1/(math.tan(math.radians(x)))

    def secrad(self, x):
        return 1/(math.cos(x))

    def cscrad(self, x):
        return 1/(math.sin(x))

    def sindeg(self, x):
        return math.sin(math.radians(x))

    def cosdeg(self, x):
        return math.cos(math.radians(x))

    def tandeg(self, x):
        return math.tan(math.radians(x))

    def cotdeg(self, x):
        return 1/(math.tan(math.radians(x)))

    def secdeg(self, x):
        return 1/(math.cos(math.radians(x)))

    def cscdeg(self, x):
        return 1/(math.sin(math.radians(x)))

    def factorial(self, x):
        return math.factorial(x)

    def logten(self, x):
        return math.log10(x)

    def logbasex(self, x, base):
        return math.log(x, base)

    def logbasee(self, x):
        return math.log(x)

    def inv_logten(self, x):
        return 1/(math.log10(x))

    # def inv_log(self, x):
    #     return math
    #
    # def invCos(self, x):
    #     return math.acos(x)
    #
    # def invTan(self, x):
    #     return math.atan(x)
    #
    # def factoria(self, x):
    #     return math.facotirs(x)
    #
    # def log_base_10(self, x):
    #     return math.log10(x)
    #
    # def inv_log_10(self, x):
    #     return 10 ** x
    #
    # def inv_log_e(self, x):
    #     return math.exp(x)
    #
    # def log_base_y(self, x, y):
    #     return math.log(x, y)