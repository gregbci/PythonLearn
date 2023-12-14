import numpy as np


a = [[1, 2], [3, 4]]
b = []

try:
   #a.extend(b)
   a += b

except Exception:
   print("invalid list data")

print(a)


c = np.array(["a", "b", "c", "d"])
d = np.array(["e", "f"])

try:
   #c = np.concatenate((c, d))
   c = np.array(list(c) + d)

except Exception:
   print("invalid numpy data")


print(c)
