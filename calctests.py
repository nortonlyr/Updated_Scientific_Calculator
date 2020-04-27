import unittest
from calculator import Calculator
import math

c = Calculator()
class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(c.add(3, 3), 6)
        self.assertEqual(c.add(10, 7), 17)

    def test_subtract(self):
        self.assertEqual(c.subtract(12, 10), 2)
        self.assertEqual(c.subtract(100, 32), 68)

    def test_multiply(self):
        self.assertEqual(c.multiply(10, 3), 30)
        self.assertEqual(c.multiply(14, 7), 98)

    def test_divide(self):
        self.assertEqual(c.divide(9, 3), 3)
        self.assertEqual(round(c.divide(100, 3), 8), 33.33333333)

    def test_square(self):
        self.assertEqual(c.square(3), 9)

    def test_exp(self):
        self.assertEqual(c.powerof(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(c.square_root(9), 3)

    def test_inv(self):
        c = Calculator()
        self.assertEqual(c.inv(4), 0.25)

    def test_sinerad(self):
        self.assertEqual(c.sinrad(30), -0.9880316240928618)
        self.assertEqual(c.sinrad(45), 0.8509035245341184)

    def test_sinedeg(self):
        self.assertEqual(round(c.sindeg(30), 2), 0.5)
        self.assertEqual(c.sindeg(60), 0.8660254037844386)

    def test_cosrad(self):
        self.assertEqual(c.cosrad(60), -0.9524129804151563)

    def test_cosdeg(self):
        self.assertEqual(round(c.cosdeg(60), 2), 0.5)

    def test_tanrad(self):
        self.assertEqual(c.tanrad(45), 1.6197751905438615)
        self.assertEqual(c.tanrad(60), 0.3200403893795629)
        self.assertEqual(c.tanrad(50), -0.2719006119976307)

    def test_tandeg(self):
        self.assertEqual(c.tandeg(60), 1.7320508075688767)
        self.assertEqual(round(c.tandeg(45), 2), 1)

    def test_cotrad(self):
        self.assertEqual(c.cotrad(50), 0.8390996311772801)

    def test_cotdeg(self):
        self.assertEqual(c.cotdeg(20), 2.7474774194546225)
        self.assertEqual(c.cotdeg(65), 0.4663076581549986)

    # def test_switch_sign(self):
    #     self.assertEqual(c.swith_sign(2), -2)

    def factorial(self):
        self.assertEqual(c.factorial(4), 24)

    def log_base_10(self):
        self.assertEqual(c.log_base_10(100), 2)

    def inv_base_10(self):
        self.assertEqual(c.inv_base_10(2), 100)

    def log_base_e(self):
        self.assertEqual(c.log_base_e(2.718281828), 1)

    def inv_base_e(self):
        self.assertEqual(c.inv_base_e(1), 2.718281828)

    # def invSin(self):
    #     self.assertEqual(c.invSin(0.5), 0.52359878)
    #
    # def invSin(self):
    #     c = Calculator()
    #     self.assertEqual(c.invSin(math.degree(0.5)), 30)
    #
    # def invCos(self):
    #     c = Calculator()
    #     self.assertEqual(c.invCos(0.5), 1.04719755)
    #
    # def invCos(self):
    #     c = Calculator()
    #     self.assertEqual(c.invCos(math.degree(0.5)), 60)
    #
    # def invTan(self):
    #     c = Calculator()
    #     self.assertEqual(c.invSin(1), 0.78539816)
    #
    # def invTan(self):
    #     c = Calculator()
    #     self.assertEqual(c.invSin(math.degree(1)), 45)

if __name__ == '__main__':
    unittest.main()
