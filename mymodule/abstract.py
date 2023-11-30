from abc import ABC, abstractmethod

class Dog(ABC):
   @abstractmethod
   def speak(self):
      pass


class Poodle(Dog):
   def __init__(self):
      self.breed = "poodle"

   def speak(self):
      print(self.breed + " woof")


dog = Poodle()
dog.speak()

