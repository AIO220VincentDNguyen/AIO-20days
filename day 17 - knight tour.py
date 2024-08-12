def is_safe(x, y, board):
    N = len(board)
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_board(board):
    for row in board:
        print('  '.join(f'{cell:2}'for cell in row))

def solve_knight_tour(N, start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board[start_x][start_y] = 1

  def solve(x, y, move_i):
    if move_i == N * N:
        return True

    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i + 1
            if solve(next_x, next_y, move_i + 1):
                return True
            board[next_x][next_y] = -1
    return False

if not solve(start_x, start_y, 1):
    print('Không có giải pháp nào tồn tại')
else:
    print_board(board)

def main():
    N = int(input("Input size of chess board: "))
    x = int(input('Input start position x: '))
    y = int(input('Input start position y: '))

    solve_knight_tour(N, x, y)

if __name__ == "__main__":
    main()