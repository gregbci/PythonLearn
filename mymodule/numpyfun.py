# don't name this file numpy as that will confuse the import
import numpy as np

a = np.array([])
b = np.array(None)
c = np.array(["a", "b", "c", "d"])
d = np.array([["e", "f"], ["g", "h"]])
e = np.array(["e", "f", "g", "h"])

array_to_test = d

if not isinstance(array_to_test, np.ndarray):
   print("invalid data")
else:
   print("valid data")

f = np.empty([0,2])
f = np.concatenate((f, d))

print(f)
