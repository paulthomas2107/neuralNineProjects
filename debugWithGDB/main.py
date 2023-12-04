import random
from itertools import combinations

random.seed(0)
items = [(f'item{i}', random.randint(1, 10), random.randint(1, 20)) for i in range(1, 201)]
max_weight = 100

best_value = 0
best_combination = []

for i in range(len(items) + 1):
    for combination in combinations(items, i):
        total_weight = sum([item[1] for item in combination])
        total_value = sum([item[2] for item in combination])

        if total_weight <= max_weight and total_value > best_value:
            print('Best: ', total_value)
            best_value = total_value
            best_combination = combination

print('Best Combination: ', best_combination)
print('Best Value: ', best_value)