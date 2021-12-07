import sys

def solve_input(input_path, solve_rows):
    with open(input_path) as rows:
        return solve_rows(rows.read().splitlines())

def solve_rows_1(rows: list):
    curr = [1 if c == '1' else -1 for c in rows[0]]
    balance = curr
    for row in rows[1:]:
        curr = [1 if c == '1' else -1 for c in row]
        balance = [a + b for a, b in zip(balance, curr)]
    epsilon, gamma = (0, 0)
    for index, v in enumerate(balance):
        gamma *= 2
        epsilon *= 2
        if v > 0:
            gamma += 1
        else:
            epsilon += 1
    return epsilon * gamma

def solve_rows_2(rows):
    c_rows = rows
    o_rows = rows

    for index in range(len(rows[0])):
        if len(c_rows) != 1:
            bit = get_least_common_bit(c_rows, index)
            c_rows = [row for row in c_rows if row[index] == bit]
        if len(o_rows) != 1:
            bit = get_most_common_bit(o_rows, index)
            o_rows = [row for row in o_rows if row[index] == bit]

    return int(c_rows[0], 2) * int(o_rows[0], 2)

def get_least_common_bit(rows: list, i: int):
    return '0' if sum([1 if r[i] == '1' else -1 for r in rows]) >= 0 else '1'

def get_most_common_bit(rows: list, i: int):
    return '1' if sum([1 if r[i] == '1' else -1 for r in rows]) >= 0 else '0'

if __name__ == '__main__':
    result = solve_input(sys.argv[1], solve_rows_1)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], solve_rows_2)
    print(f'Part 2: {result}')
