from RandomNumberGenerator import RandomNumberGenerator
from Calculator import Calculator


class PopulationSampling:
    def __init__(self):
        pass

    def simple_random(self, lst, n, s):
        random_generator = RandomNumberGenerator()
        simple_random_sample = random_generator.random_choices_seed(self, lst, n, s)
        return simple_random_sample

    def margin_error(self, lst):
        calculator = Calculator()
        standard_deviation = calculator.standard_deviation(lst)
        n = len(lst)
        return 1.96 * (standard_deviation / calculator.square_root(n))

    def confidence_interval(self, lst):
        calculator = Calculator()
        standard_deviation = calculator.standard_deviation(lst)
        n = len(lst)
        mean = calculator.mean(lst)
        margin_error = 1.96 * (standard_deviation / calculator.square_root(n))
        confidence_interval = [round(mean+margin_error, 6), round(mean-margin_error, 6)]
        return confidence_interval