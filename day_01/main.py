def process_calories(input_path: str) -> list[int]:
    with open(input_path, encoding="utf-8") as f:
        elves = f.read().split('\n\n')
        return [sum([int(line) for line in elf.strip().split('\n')]) for elf in elves]


def part_two(input_path: str) -> int:
    calories_list = process_calories(input_path)
    return sum(sorted(calories_list, reverse=True)[0:3])


def part_one(input_path: str) -> int:
    calories_list = process_calories(input_path)
    max = 0
    for calories in calories_list:
        if calories > max:
            max = calories
    return max


if __name__ == '__main__':
    input_path = './day_01/input.txt'
    print(f'---Part One---\n{part_one(input_path)}')
    print(f'---Part Two---\n{part_two(input_path)}')
