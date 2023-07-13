import unittest

class TestNumMethods(unittest.TestCase):

   def test_upper(self):
      a = -100.0
      b = 50.0
      self.assertEqual(abs(a), 100.0);
      self.assertEqual(abs(b), 50.0);

if __name__ == '__main__':
   unittest.main()

