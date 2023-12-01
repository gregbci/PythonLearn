from abc import ABC, abstractmethod

class Dog(ABC):
   @abstractmethod
   def speak(self):
      pass

   @property
   @abstractmethod
   def breed(self) -> str:
      pass


class Poodle(Dog):
   def __init__(self):
      self.__breed = "poodle"

   def speak(self):
      print(self.__breed + " woof")

   @property
   def breed(self) -> str:
      return self.__breed

dog = Poodle()     #  <-- can't instantiate if Dog isn't implemented completely
dog.speak()        
print(dog.breed)   #  <-- this behaves just like a variable

# dog.breed = "cabbage"  #  <-- this fails because property is readonly

