import sys

def load_game(input_path: str) -> tuple:
    with open(input_path, 'r') as f:
        draws = [int(d) for d in f.readline().split(',')]
        boards = []
        for l in f.readlines():
            if l == '\n':
                boards.append([])
            else:
                boards[-1].append([int(c) for c in l.split()])
        return draws, boards

def mark_draw(board, draw: int) -> tuple:
    is_winning = False
    size = len(board[0])
    score = 0
    for row, b_row in enumerate(board):
        for column, b_number in enumerate(b_row):
            if board[row][column] == draw:
                board[row][column] = -1
                is_winning = is_winning or (sum([i[column] for i in board]) == -size)
            elif board[row][column] != -1:
                score += board[row][column]
        is_winning = is_winning or (sum(board[row]) == -size)

    return score * draw, is_winning

def solve_input_1(input_path: str) -> int:
    draws, boards = load_game(input_path)
    for draw in draws:
        for board in boards:
            score, is_winning = mark_draw(board, draw)
            if is_winning:
                return score

def solve_input_2(input_path: str) -> int:
    draws, boards = load_game(input_path)
    winning_boards = [False] * len(boards)
    for draw in draws:
        for index, board in enumerate(boards):
            if winning_boards[index]:
                continue
            score, is_winning = mark_draw(board, draw)
            winning_boards[index] = is_winning
            if all(winning_boards):
                return score

if __name__ == '__main__':
    result = solve_input_1(sys.argv[1])
    print(f'Part 1: {result}')
    result = solve_input_2(sys.argv[1])
    print(f'Part 2: {result}')
