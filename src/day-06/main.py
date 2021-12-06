import sys
from collections import deque


def sim_school(school: deque, days: int) -> int:
    for day in range(days):
        fresh_fish = school.popleft()
        school.append(fresh_fish)
        school[6] += fresh_fish
    return school


def solve_input(input_path: str, days: int):
    with open(input_path, 'r') as infile:
        school = deque([0, 0, 0, 0, 0, 0, 0, 0, 0])
        for fish in infile.readline().split(','):
            school[int(fish)] += 1
        return sum(sim_school(school, days))


if __name__ == '__main__':
    result = solve_input(sys.argv[1], 80)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], 256)
    print(f'Part 2: {result}')
