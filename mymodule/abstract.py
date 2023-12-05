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

class Labrador(Dog):
   def speak(self):
      print(self.breed + " woof")

   breed: str = "Labrador"



poodle = Poodle()     #  <-- can't instantiate if Dog isn't implemented completely
poodle.speak()        
print(poodle.breed)   #  <-- this behaves just like a variable
# poodle.breed = "cabbage"  #  <-- this fails because property is readonly

lab = Labrador()
lab.speak()
print(lab.breed)


