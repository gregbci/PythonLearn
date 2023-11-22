import unittest

class Dog(object):

   # These are a "class" variable in python, not an instance variable, sort of
   # You can change this before creating an instance, and the instance gets the
   # change, but previous isntances won't
   breed = "lab"

   def __init__(self, name):
      self.name = name
      self.isHappy = False

   def praise(self):
      self.isHappy = True 

   def _protected(self):
      print("dog's protected method")


class SubDog(Dog):
   def praise(self):
      self._protected()


class TestDog(unittest.TestCase):

   def test_dog_can_make_dog_happy(self):
      dog = Dog("fido")
      dog.praise()
      self.assertTrue(dog.isHappy)

   def test_dogs_can_have_unique_names(self):
      a = Dog("daisy")
      b = Dog("molly")
      self.assertEqual(a.name, "daisy")
      self.assertNotEqual(a.name, b.name)

   # test how a "class" variable works in Python.  It appears that a class
   # variable is sort of like a default value for init.  You can change the
   # class variable and all instances get the change.  However, here's where
   # it's screwy.  Because Python will just let you create a variable at runtime
   # assinging an instance variable "hides" the class variable.  For example
   # dog.breed = "mutt" creates an instance variable that "hides" the class.
   # any Dog instance that didn't change breed will reference the class variable.
   # This demonstrates how "scripty" Python is.  Objects are just dictionaries,
   # similar to how Perl does it.  Very shallow OO, so be careful with design
   # assumptions.
   def test_dogs_can_sort_of_have_unique_breed(self):
       a = Dog("daisy")
       b = Dog("molly")
       c = Dog("ruby")

       a.breed = "retriever"
       self.assertEqual(a.breed, "retriever")
       self.assertEqual(b.breed, "lab")
       self.assertEqual(c.breed, "lab")

       c.breed = "poodle"
       self.assertEqual(a.breed, "retriever")
       self.assertEqual(b.breed, "lab")
       self.assertEqual(c.breed, "poodle")

       Dog.breed = "terrier"
       self.assertEqual(a.breed, "retriever") #  <--- hidden with instance variable
       self.assertEqual(b.breed, "terrier")   #  <--- class variable changed
       self.assertEqual(c.breed, "poodle")    #  <--- hidden with instance variable
  
   def test_sub_dog(self):
      a = SubDog("sub")
      a.praise()

 
