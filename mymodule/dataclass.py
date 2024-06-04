from dataclasses import dataclass, field

@dataclass
class Prediction:
    label: str
    probability: float
    horse: [] = field(default_factory=list)

def predict() -> Prediction:
    return Prediction("foo", 0.7)

p = predict()
print(p)

