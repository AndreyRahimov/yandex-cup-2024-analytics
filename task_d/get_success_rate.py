from itertools import product

roll_combinations: list[tuple] = list(product(range(1, 7), repeat=5))
roll_results = []

for roll in roll_combinations:
    if 1 in roll or 5 in roll:
        roll_results.append(True)
        continue

    res = False

    for i in (2, 3, 4, 6):
        if roll.count(i) >= 3:
            res = True
            break

    roll_results.append(res)

print(sum(roll_results))
