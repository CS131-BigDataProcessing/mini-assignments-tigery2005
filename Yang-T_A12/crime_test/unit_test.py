from stats_function import get_mean, get_median
from validate_functions import is_sex_valid, is_age_valid
import unittest
import math

class TestFunctions(unittest.TestCase):
	def test_mean(self):
		result = get_mean()
		self.assertFalse(math.isnan(result), "Result is NaN")
		self.assertGreaterEqual(result, 1, "Value is less than 1")
		self.assertLessEqual(result, 100, "Value is greater than 100")

	def test_median(self):
		result = get_median()
		self.assertFalse(math.isnan(result), "Result is NaN")
		self.assertGreaterEqual(result, 1, "Value is less than 1")
		self.assertLessEqual(result, 100, "Value is greater than 100")

	def test_sex_valid(self):
		result = is_sex_valid()
		self.assertTrue(result, "There are invalid sex entries")
	
	def test_age_valid(self):
		result = is_age_valid()
		self.assertTrue(result, "There are invalid age entries")



if __name__ == '__main__':
	unittest.main()


