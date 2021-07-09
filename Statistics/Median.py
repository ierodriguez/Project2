class Median:
    result = 0

    def __init__(self):
        pass

    def median(self, values):
        values.sort()
        length = len(values)
        if (length % 2) == 0:
            self.result = ((values[length // 2]) + (values[(length // 2) - 1])) / 2
            return self.result
        else:
            self.result = values[(length // 2)]
            return self.result