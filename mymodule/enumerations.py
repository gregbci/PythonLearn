from enum import Enum

class TrainingLabels(Enum):
    Rest = 0
    Action = 1


print(f"length:", len(TrainingLabels))
print(f"name:", TrainingLabels.Rest)
print(f"value:", TrainingLabels.Rest.value)

