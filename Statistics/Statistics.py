from Statistics.mean import Mean
from Statistics.median import Median
from Statistics.std_dev import StandardDeviation
from Statistics.mode import Mode
from Statistics.variance import Variance


class Calculator:
    result = 0

    def __init__(self):
        pass

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
