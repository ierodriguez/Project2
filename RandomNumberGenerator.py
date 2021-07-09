import random

class RandomGenerator:
    def __init__(self):
        pass

    def random(self, a, b):
        return random.randrange(a, b)

    def random_seed(self, a, b, seed):
        random.seed(seed)
        return random.randrange(a, b)

    def random_list(self, a, b, n, seed):
        random.seed(seed)
        random_list = []
        for value in range(n):
            random_list.append(random.randrange(a, b))
        return random_list

    def random_choice(self, lst):
        return random.choice(lst)

    def random_choice_seed(self, lst, seed):
        random.seed(seed)
        return random.choice(lst)

    def random_choices(self, lst, n):
        return random.choices(lst, k=n)

    def random_choices_seed(self, lst, n, seed):
        random.seed(seed)
        return random.choices(lst, k=n)