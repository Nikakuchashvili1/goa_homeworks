import random
import itertools

elements = [1, 2, 3, 4, 5]

random.shuffle(elements)

cycle_iterator = itertools.cycle(elements)

for _ in range(15):
    print(next(cycle_iterator))