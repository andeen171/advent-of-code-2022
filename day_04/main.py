def get_positions(line: str):
    pair = line.strip().split(',')
    p1 = [int(cordinate)
                    for cordinate in pair.pop().split('-')]
    p2= [int(cordinate)
                    for cordinate in pair.pop().split('-')]
    return p1, p2


def part_one(pairs: list[str]) -> int:
    count = 0
    for pair in pairs:
        position_one, position_two = get_positions(pair)
        if (position_one[0] >= position_two[0]) and (position_one[1] <= position_two[1]):
            count += 1
        elif (position_two[0] >= position_one[0]) and (position_two[1] <= position_one[1]):
            count += 1
    return count


def do_overlap(p1, p2):
    if (p1 >= p2[0]) and (p1 <= p2[1]):
        return True
    return False


def part_two(pairs: list[str]) -> int:
    count = 0
    for pair in pairs:
        position_one, position_two = get_positions(pair)
        if (position_one[0] >= position_two[0]) and (position_one[0] <= position_two[1]):
            count += 1
        elif (position_one[1] >= position_two[0]) and (position_one[1] <= position_two[1]):
            count += 1
        elif (position_two[0] >= position_one[0]) and (position_two[0] <= position_one[1]):
            count += 1
        elif (position_two[1] >= position_one[0]) and (position_two[1] <= position_one[1]):
            count += 1
    return count


def process_pairs(input_path: str) -> list[str]:
    with open(input_path, encoding='utf-8') as f:
        return f.readlines()


if __name__ == "__main__":
    pairs = process_pairs("./day_04/input.txt")
    print(f'---Part One---')
    print(part_one(pairs))
    print(f'---Part Two---')
    print(part_two(pairs))
