from itertools import product

roll_combinations: list[tuple] = list(product(range(1, 7), repeat=5))
roll_results = []

for roll in roll_combinations:
    roll_res = 0

    for i in range(1, 7):
        if (value_count := roll.count(i)) >= 3:
            match i:
                case 1:
                    match value_count:
                        case 3:
                            roll_res += 100

                        case 4:
                            roll_res += 300

                        case 5:
                            roll_res += 1_200

                case 2:
                    match value_count:
                        case 3:
                            roll_res += 20

                        case 4:
                            roll_res += 60

                        case 5:
                            roll_res += 240

                case 3:
                    match value_count:
                        case 3:
                            roll_res += 30

                        case 4:
                            roll_res += 90

                        case 5:
                            roll_res += 360

                case 4:
                    match value_count:
                        case 3:
                            roll_res += 40

                        case 4:
                            roll_res += 120

                        case 5:
                            roll_res += 480

                case 5:
                    match value_count:
                        case 3:
                            roll_res += 50

                        case 4:
                            roll_res += 150

                        case 5:
                            roll_res += 600

                case 6:
                    match value_count:
                        case 3:
                            roll_res += 60

                        case 4:
                            roll_res += 180

                        case 5:
                            roll_res += 720

    if roll_res:
        roll_results.append(roll_res)
        continue

    roll_res = (roll.count(1) * 10) + (roll.count(5) * 5)

    if roll_res:
        roll_results.append(roll_res)

print(sum(roll_results) / len(roll_results))

print(sum(roll_results))
