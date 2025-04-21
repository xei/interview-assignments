import unittest
from .core import find_best_threshold

class BestThresholdTestCase(unittest.TestCase):
    def test_basic_case(self):
        data = {
            0.1: {"tp": 90, "fp": 10, "tn": 80, "fn": 5},
            0.2: {"tp": 85, "fp": 5, "tn": 82, "fn": 10},
            0.3: {"tp": 60, "fp": 2, "tn": 90, "fn": 40},
        }
        self.assertEqual(find_best_threshold(data), 0.1)

    def test_no_valid_threshold(self):
        data = {
            0.1: {"tp": 30, "fp": 10, "tn": 50, "fn": 50},
            0.2: {"tp": 20, "fp": 15, "tn": 45, "fn": 60},
        }
        self.assertIsNone(find_best_threshold(data))

if __name__ == "__main__":
    unittest.main()