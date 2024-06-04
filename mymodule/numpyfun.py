# don't name this file numpy as that will confuse the import
import numpy as np

import sys

a = np.array(None)
b = np.array([])
c = np.array([[]])
d = np.array([["e", "f"], ["g", "h"]])
e = np.array(["e", "f", "g", "h"])

print(a.ndim, a.shape)
print(b.ndim, b.shape)
print(c.ndim, c.shape)
print(d.ndim, d.shape)
print(e.ndim, e.shape)

array_to_test = d
if not isinstance(array_to_test, np.ndarray):
    print("invalid data")
else:
    print("valid data")

f = np.empty([0, 2])
f = np.concatenate((f, d))

print(np.zeros((4, 2)))


print(sys.float_info)


