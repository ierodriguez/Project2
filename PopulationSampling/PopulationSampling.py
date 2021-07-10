from RNG.RandomNumberGenerator import RandomNumberGenerator
from Calculator.calculator import Calculator


class PopulationSampling:
    def __init__(self):
        pass

    @staticmethod
    def simple_rand(self, lst, n, s):
        random_generator = RandomNumberGenerator()
        simple_random_sample = random_generator.rand_choices_seed(self, lst, n, s)
        return simple_random_sample

    @staticmethod
    def margin_error(self, lst):
        calculator = Calculator()
        std_dev = calculator.standard_dev(lst)
        n = len(lst)
        return 1.96 * (std_dev / calculator.squareroot(n))

    @staticmethod
    def confidence_interval(self, lst):
        calculator = Calculator()
        std_dev = calculator.standard_dev(lst)
        n = len(lst)
        mean = calculator.mean(lst)
        margin_err = 1.96 * (std_dev / calculator.squareroot(n))
        confidence_int = [round(mean+margin_err, 6), round(mean-margin_err, 6)]
        return confidence_int
