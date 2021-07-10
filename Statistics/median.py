class Median:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def median(self, values):
        values.sort()  # sorts values numerically
        length = len(values)
        if (length % 2) == 0:  # checks if amount of values is even
            self.result = ((values[length // 2]) + (values[(length // 2) - 1])) / 2
            return self.result
        else:
            self.result = values[(length // 2)]
            return self.result
