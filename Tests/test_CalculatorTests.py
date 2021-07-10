import unittest
from Calculator.calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.testData = CsvReader("Tests/Data/Unit Test Addition.csv")

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def test_subtract_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Subtraction.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def test_multiply_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Multiplication.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def test_divide_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Division.csv").data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def test_square_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Square.csv").data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def test_squareroot_method_calculator(self):
        test_data = CsvReader("Tests/Data/Unit Test Square Root.csv").data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.squareroot(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
            pprint(row)

    def tearDown(self) -> None:
        # self.calculator.dispose()
        pass


if __name__ == '__main__':
    unittest.main()
