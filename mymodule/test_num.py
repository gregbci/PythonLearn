import unittest

class TestNumMethods(unittest.TestCase):

   def test_abs_of_positive_is_positive(self):
      value = 50.0
      self.assertEqual(abs(value), 50.0);

   def test_abs_of_negative_is_positive(self):
      value = -100.0
      self.assertEqual(abs(value), 100.0);

