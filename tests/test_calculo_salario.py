import unittest
from domain.calculo_salario import calculate_salary

class MyTestCase(unittest.TestCase):
    def test_calculate_inss(self):
        calculo_salario = calculate_salary(1600)
        inss = calculo_salario.calculate_inss()
        self.assertEqual(inss, 128)  # add assertion here


if __name__ == '__main__':
    unittest.main()
