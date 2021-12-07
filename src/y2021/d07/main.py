import sys
from math import ceil, floor


def solve_input(input_path: str, solve_crabs) -> int:
    with open(input_path, 'r') as infile:
        crabs = []
        for crab in infile.readline().strip().split(','):
            crabs.append(int(crab))
        return solve_crabs(crabs)


def solve_crabs_1(crabs: list):
    crabs_sorted = sorted(crabs)
    depth = crabs_sorted[len(crabs)//2]
    return sum([abs(depth - c) for c in crabs])


def solve_crabs_2(crabs: list):
    avg = sum(crabs) / len(crabs)
    avg_ceil = ceil(avg)
    avg_floor = floor(avg)
    r1 = sum([(abs(c - avg_ceil) * (abs(c - avg_ceil)+1)) // 2 for c in crabs])
    r2 = sum([(abs(c - avg_floor) * (abs(c - avg_floor)+1)) // 2 for c in crabs])
    return min(r1, r2)


if __name__ == '__main__':
    result = solve_input(sys.argv[1], solve_crabs_1)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], solve_crabs_2)
    print(f'Part 2: {result}')
