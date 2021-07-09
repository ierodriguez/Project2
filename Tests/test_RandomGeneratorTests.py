import unittest

from RandomNumberGenerator import RandomNumberGenerator


class RandomGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = RandomNumberGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random_generator, RandomNumberGenerator)

    def test_random_number_without_seed(self):
        random_generator = RandomNumberGenerator()
        print(random_generator.random(self, 0, 100))

    def test_random_number_with_seed(self):
        random_generator = RandomNumberGenerator()
        random_number = random_generator.random_seed(self, 0, 100, 10)
        self.assertEqual(random_generator.random_seed(self, 0, 100, 10), random_number)

    def test_random_list_with_seed(self):
        random_generator = RandomNumberGenerator()
        random_list = random_generator.random_list(self, 0, 100, 10, 5)
        self.assertEqual(random_generator.random_list(self, 0, 100, 10, 5), random_list)

    def test_random_choice_without_seed(self):
        random_generator = RandomNumberGenerator()
        values = [7, 20, 55, 14, 34, 78]
        random_choice = random_generator.random_choice(self, values)
        print(random_choice)

    def test_random_choice_with_seed(self):
        random_generator = RandomNumberGenerator()
        values = [8, 21, 56, 15, 35, 79]
        random_choice = random_generator.random_choice_seed(self, values, 5)
        self.assertEqual(random_generator.random_choice_seed(self, values, 5), random_choice)

    def test_random_choices_without_seed(self):
        random_generator = RandomNumberGenerator()
        values = [4, 34, 15, 47, 22, 70]
        random_choices = random_generator.random_choices(self, values, 3)
        print(random_choices)

    def test_random_choices_with_seed(self):
        random_generator = RandomNumberGenerator()
        values = [5, 35, 16, 48, 23, 71]
        random_choices = random_generator.random_choices_seed(self, values, 4, 7)
        self.assertEqual(random_generator.random_choices_seed(self, values, 4, 7), random_choices)