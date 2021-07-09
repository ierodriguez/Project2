class Variance:
    result = 0

    def __init__(self):
        pass

    def variance(self, values):
        values_mean = sum(values) / len(values)
        self.result = sum([((x - values_mean) ** 2) for x in values]) / len(values)
        return self.result