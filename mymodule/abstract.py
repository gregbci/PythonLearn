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

   def speak(self):
      print(self.breed + " woof")

   @property
   def breed(self) -> str:
      return "poodle"

dog = Poodle()     #  <-- can't instantiate if Dog isn't implemented completely
dog.speak()        
print(dog.breed)   #  <-- this behaves just like a variable

# dog.breed = "cabbage"  #  <-- this fails because property is readonly

