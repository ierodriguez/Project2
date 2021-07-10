from Calculator.addition import addition
from Calculator.division import division
from Calculator.multiplication import multiplication
from Calculator.square import square
from Calculator.squareRoot import squareroot
from Calculator.subtraction import subtraction
from Statistics.mean import Mean
from Statistics.median import Median
from Statistics.std_dev import StandardDeviation
from Statistics.mode import Mode
from Statistics.variance import Variance


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

    def mean(self, values):
        self.result = Mean.mean(self, values)
        return self.result

    def median(self, values):
        self.result = Median.median(self, values)
        return self.result

    def mode(self, values):
        self.result = Mode.mode(self, values)
        return self.result

    def standard_dev(self, values):
        self.result = StandardDeviation.standard_deviation(self, values)
        return self.result

    def variance(self, values):
        self.result = Variance.variance(self, values)
        return self.result
