import unittest

class Dog(object):
   def __init__(self, name):
      self.name = name
      self.isHappy = False

   def praise(self):
      self.isHappy = True 


class TestDog(unittest.TestCase):

   def test_dog_can_make_dog_happy(self):
      dog = Dog("fido")
      dog.praise()
      self.assertTrue(dog.isHappy)


