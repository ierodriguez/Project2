class StandardDeviation:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def standard_deviation(self, values):
        values_mean = sum(values) / len(values)
        self.result = (sum([((x - values_mean) ** 2) for x in values]) / len(values)) ** 0.5
        return self.result
