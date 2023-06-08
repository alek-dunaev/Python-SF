import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_division_success(self):
        assert self.calc.division(self, 10, 2 ) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 15, 3) == 12

    def test_multiply(self):
        assert self.calc.multiply(self, 10 , 3) == 30

    def teardown(self):
        print(' Выполнение метода Teardown')
