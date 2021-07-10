import unittest

from RNG.RandomNumberGenerator import RandomNumberGenerator
from PopulationSampling.PopulationSampling import PopulationSampling


class PopulationSamplingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.random_generator = RandomNumberGenerator()
        self.population_sampling = PopulationSampling()

    def test_instantiate_pop_sampling(self):
        self.assertIsInstance(self.population_sampling, PopulationSampling)

    def test_instantiate_rand_gen(self):
        self.assertIsInstance(self.random_generator, RandomNumberGenerator)

    def test_simple_rand(self):
        test_list = self.random_generator.rand_list(self, 0, 10, 50, 3)
        result = self.population_sampling.simple_rand(self, test_list, 10, 5)
        self.assertEqual(self.population_sampling.simple_rand(self, test_list, 10, 5), result)
        test_list.clear()

    def test_margin_error(self):
        test_list = [4, 9, 3, 6, 8, 2, 1, 8, 5, 9]
        self.assertEqual(round(self.population_sampling.margin_error(self, test_list), 6), 1.8305)
        test_list.clear()

    def test_confidence_interval(self):
        test_list = [4, 9, 3, 6, 8, 2, 1, 8, 5, 9]
        self.assertEqual(self.population_sampling.confidence_interval(self, test_list), [7.3305, 3.6695])
        test_list.clear()


if __name__ == "__main__":
    unittest.main()
