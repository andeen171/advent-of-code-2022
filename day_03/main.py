import string

def find_misplaced(line: str) -> str:
    middle = int(len(line) / 2 + 1) - 1
    return list(set(line[:middle]).intersection(line[middle:]))[0]

def get_char_value(char: str) -> int:
    if char.isupper():
        return string.ascii_uppercase.index(char) + 27
    return string.ascii_lowercase.index(char) + 1

def part_one(rucksacks: list[str]) -> int:
    return sum([get_char_value(find_misplaced(rucksack)) for rucksack in rucksacks])


def find_badge(rucksacks: list[str]) -> str:
    return list(set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2]))[0]


def part_two(rucksacks: list[str]) -> int:
    sum = 0
    for x in range(0, len(rucksacks) - 1, 3):
        sum += get_char_value(find_badge(rucksacks[x:x + 3]))
    return sum


def get_rucksacks(input_path: str) -> list[str]:
    with open(input_path, encoding='utf-8') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

if __name__ == "__main__":
    rucksacks = get_rucksacks("./day_03/input.txt")
    print(f'---Part One---\n{part_one(rucksacks)}')
    print(f'---Part Two---\n{part_two(rucksacks)}')
