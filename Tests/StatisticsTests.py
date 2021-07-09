import unittest

from Calculator import Calculator
from RandomNumberGenerator import RandomNumberGenerator


class StatCalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_mean_method_calculator(self):
        calculator = Calculator()
        random_generator = RandomNumberGenerator()
        test_list = random_generator.random_list(self, 0, 100, 5, 3)
        mean = calculator.mean(test_list)
        self.assertEqual(calculator.mean(test_list), mean)
        self.assertEqual(calculator.result, mean)
        test_list.clear()

    def test_median_method_calculator(self):
        calculator = Calculator()
        random_generator = RandomNumberGenerator()
        test_list = random_generator.random_list(self, 0, 100, 5, 3)
        median = calculator.median(test_list)
        self.assertEqual(calculator.median(test_list), median)
        self.assertEqual(calculator.result, median)
        test_list.clear()

    def test_mode_method_calculator(self):
        calculator = Calculator()
        random_generator = RandomNumberGenerator()
        test_list = random_generator.random_list(self, 0, 100, 5, 3)
        values_mode = calculator.mode(test_list)
        self.assertEqual(calculator.mode(test_list), values_mode)
        self.assertEqual(calculator.result, values_mode)
        test_list.clear()

    def test_std_dev_method_calculator(self):
        calculator = Calculator()
        random_generator = RandomNumberGenerator()
        test_list = random_generator.random_list(self, 0, 100, 5, 3)
        standard_deviation = calculator.standard_deviation(test_list)
        self.assertEqual(calculator.standard_dev(test_list), standard_deviation)
        self.assertEqual(calculator.result, standard_deviation)

    def test_variance_method_calculator(self):
        calculator = Calculator()
        random_generator = RandomNumberGenerator()
        test_list = random_generator.random_list(self, 0, 100, 5, 3)
        variance = calculator.variance(test_list)
        self.assertEqual(calculator.variance(test_list), variance)
        self.assertEqual(calculator.result, variance)

if __name__ == "__main__":
    unittest.main()