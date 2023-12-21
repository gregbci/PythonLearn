from dataclasses import dataclass

@dataclass
class Prediction:
    label: str
    probability: float

def predict() -> Prediction:
    return Prediction("foo", 0.7)

p = predict()
print(p.label)

