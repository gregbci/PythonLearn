import unittest

class TestNumMethods(unittest.TestCase):

   def test_abs_positive(self):
      value = 50.0
      self.assertEqual(abs(value), 50.0);

   def test_abs_negative(self):
      value = -100.0
      self.assertEqual(abs(value), 100.0);
