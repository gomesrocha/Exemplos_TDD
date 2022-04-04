import unittest
from domain.calculo_salario import calculateSalary

class MyTestCase(unittest.TestCase):
    def test_calculate_inss(self):
        inss = calculateSalary.calculate_inss(1600)
        self.assertEqual(inss, 128)  # add assertion here


if __name__ == '__main__':
    unittest.main()
