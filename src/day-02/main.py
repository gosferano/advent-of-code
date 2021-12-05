import sys

def solve_input(input_path, solve_rows):
    with open(input_path) as rows:
        return solve_rows(rows)

def solve_rows_1(rows):
    h, v = (0, 0)
    for row in rows:
        val = int(row.split(' ')[1])
        if row[0] == 'f': h += val
        if row[0] == 'd': v += val
        if row[0] == 'u': v -= val
    return h * v

def solve_rows_2(rows):
    h, v, aim = (0, 0, 0)
    for row in rows:
        val = int(row.split(' ')[1])
        if row[0] == 'f':
            h += val
            v += val * aim
        if row[0] == 'd': aim += val
        if row[0] == 'u': aim -= val
    return h * v

if __name__ == '__main__':
    result = solve_input(sys.argv[1], solve_rows_1)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], solve_rows_2)
    print(f'Part 2: {result}')
