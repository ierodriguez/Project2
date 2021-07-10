class Mode:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def mode(self, values):
        counter = {}
        mode = []
        highest_repeat = 0  # counter for highest repeat
        for num in values:  # adds the values to a counter
            if num in counter.keys():
                counter[num] += 1
                if counter.get(num) > highest_repeat:
                    highest_repeat = counter.get(num)
            else:
                counter[num] = 1

        if highest_repeat > 1:
            for num in counter.keys():
                if counter.get(num) == highest_repeat:
                    mode.append(num)
        else:
            return None

        self.result = mode
        return self.result
