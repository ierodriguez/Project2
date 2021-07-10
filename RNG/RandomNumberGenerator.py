import random


class RandomNumberGenerator:
    def __init__(self):
        pass

    @staticmethod
    def rand(self, a, b):
        return random.randrange(a, b)

    @staticmethod
    def rand_seed(self, a, b, seed):
        random.seed(seed)
        return random.randrange(a, b)

    @staticmethod
    def rand_list(self, a, b, n, seed):
        random.seed(seed)
        random_list = []
        for value in range(n):
            random_list.append(random.randrange(a, b))
        return random_list

    @staticmethod
    def rand_choice(self, lst):
        return random.choice(lst)

    @staticmethod
    def rand_choice_seed(self, lst, seed):
        random.seed(seed)
        return random.choice(lst)

    @staticmethod
    def rand_choices(self, lst, n):
        return random.choices(lst, k=n)

    @staticmethod
    def rand_choices_seed(self, lst, n, seed):
        random.seed(seed)
        return random.choices(lst, k=n)
