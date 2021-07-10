class Mean:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def mean(self, values):
        self.result = sum(values) / len(values)
        return self.result
