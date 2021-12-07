import sys
from itertools import cycle

def get_range(a, b):
    return range(a, b+1, 1) if a <= b else range(a, b-1, -1)

def get_line(x1, y1, x2, y2, diagonal: bool):
    if x1 == x2:
        return [(x1, y) for y in get_range(y1, y2)]
    if y1 == y2:
        return [(x, y1) for x in get_range(x1, x2)]
    if not diagonal:
        return []
    return [(x, y) for x, y in zip(get_range(x1, x2), get_range(y1, y2))]

def solve_input(input_path, diagonal: bool):
    field = {}
    with open(input_path) as rows:
        for row in rows:
            x1, y1, x2, y2 = [int(c) for c in row.strip().replace(' -> ', ',').split(',')]
            for coords in get_line(x1, y1, x2, y2, diagonal):
                if coords not in field:
                    field[coords] = 0
                field[coords] += 1
    return len([v for v in field.values() if v > 1])

if __name__ == '__main__':
    result = solve_input(sys.argv[1], False)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], True)
    print(f'Part 2: {result}')
