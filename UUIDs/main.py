import pandas as pd
import uuid

data = pd.DataFrame({
    "id":  [uuid.uuid4() for _ in range(6)],
    "value": [40, 20, 10, 20, 30, 30],
    "value2": [1, 1, 1, 0, 0, 1]
})

data = data.set_index('id')
existing = pd.read_csv("file.csv")
existing = existing.set_index("id")

combine = pd.concat([existing, data], verify_integrity=True)
print(combine)

test = uuid.uuid4()
for _ in range(9000000):
    if uuid.uuid4() == test:
        print("Match")
print("Completed")
