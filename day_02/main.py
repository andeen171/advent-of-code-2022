# AX = Rock, BY = Paper, CZ = Scissors
# Rock = 1, Paper = 2, Scissors = 3
# Loss = 0, Draw = 3, Win = 6
optionScore = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "Y": "A",
    "X": "C",
    "Z": "B",
}

playerOption = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def getOptionValue(option: str) -> int:
    match option:
        case "A" | "X":
            return 1
        case "B" | "Y":
            return 2
        case "C" | "Z":
            return 3


def get_game_score(input_path: str) -> list[str]:
    with open(input_path, "r") as f:
        return f.read().split("\n")

def getMatchupScore(x_choice: str, y_choice: str) -> int:
    if optionScore[y_choice] == x_choice:
        return 0
    elif optionScore[x_choice] == y_choice:
        return 6
    return 3


def part_one(lines: list[str]):
    score = 0
    for line in lines:
        options = line.split()
        score += getOptionValue(options[1]) + getMatchupScore(options[1], options[0])
    return score


def part_two(lines: list[str]):
    score = 0
    for line in lines:
        options = line.split()
        if options[1] == 'X':
            score += getOptionValue(optionScore[options[0]])
        elif options[1] == 'Y':
            score += getOptionValue(options[0]) + 3
        else:
            score += getOptionValue(optionScore[optionScore[options[0]]]) + 6
    return score
    


if __name__ == '__main__':
    lines = get_game_score("./day_02/input.txt")
    print(f'----Part One----\n{part_one(lines)}')
    print(f'----Part Two----\n{part_two(lines)}')
