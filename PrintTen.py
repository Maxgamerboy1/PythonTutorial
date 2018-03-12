import random

LIMIT = 10000
i = 0
while i < LIMIT:
    rand = random.randint(0, 1)
    if rand > .7:
        print('/', end='')
    else:
        print("\\", end='')
    if i % 120 == 0:
        print()
    i += 1
