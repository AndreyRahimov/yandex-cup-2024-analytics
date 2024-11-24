from itertools import product


def play_game(goal, progress, combination, turn):
    toss = combination[turn]

    if toss:
        progress += 1

    else:
        goal += 1
        progress = 0

    if progress == goal:
        return True

    turn += 1
    turns_left = 10 - turn

    if goal - progress > turns_left:
        return False

    return play_game(goal, progress, combination, turn)


tosses_combinations = list(product((True, False), repeat=10))
combinations_results = []

for combination in tosses_combinations:
    combinations_results.append(play_game(2, 0, combination, 0))

win_rate = sum(combinations_results) / len(combinations_results)
print(win_rate)
