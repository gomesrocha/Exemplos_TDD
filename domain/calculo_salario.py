class calculate_salary:
    def __init__(self, gross_salary):
        self.gross_salary = gross_salary

    def calculate_inss(self):
        if self.gross_salary < 1693.73:
            inss = self.gross_salary * 8 / 100
        elif self.gross_salary >= 1693.73 and self.gross_salary < 2822.91:
            inss = self.gross_salary * 9 / 100
        elif self.gross_salary > 2822.90 and self.gross_salary < 5645.80:
            inss = self.gross_salary * 11 / 100
        else:
            inss = 621.03
        return inss

    def calculate_irrf(self):
        salary = self.gross_salary - calculate_salary.calculate_inss()
        if salary >= 1903.99 and salary < 2826.66:
            irrf = (salary - 142.82) * 7.5 / 100
        elif salary >= 2826.66 and salary < 3751.06:
            irrf = (salary - 354.80) * 15 / 100
        elif salary >= 3751.05 and salary < 4664.69:
            irrf = (salary - 636.13) * 22.5 / 100
        elif salary >= 4664.69:
            irrf = (salary - 869.36) * 27.5 / 100
        return irrf
