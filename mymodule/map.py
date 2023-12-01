names = ["Foo", "Bar", "Baz"]
lowercase = list(map(str.lower, names))
print(lowercase)

data = [["Foo", 1], ["Bar", 2], ["Baz", 3]]

names = [x[0] for x in data]
nums = [x[1] for x in data]
print(names)
print(nums)
