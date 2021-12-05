import sys

def solve_input(input_path, window_size:int):
    with open(input_path) as rows:
        return solve_rows(rows, window_size)

def solve_rows(rows, window_size:int):
    result = 0
    p = []
    for row in rows:
        p.append(int(row))
        if len(p) > window_size:
            if p[window_size] > p[0]: result += 1
            p.pop(0)
    return result

if __name__ == '__main__':
    result = solve_input(sys.argv[1], 1)
    print(f'Part 1: {result}')
    result = solve_input(sys.argv[1], 3)
    print(f'Part 2: {result}')
