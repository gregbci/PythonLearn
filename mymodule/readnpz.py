import numpy as np

file = "/Users/gregwilding/Downloads/test.npz"
data = np.load(file)

print(data["X"])
print(data["y"])

data.close()
