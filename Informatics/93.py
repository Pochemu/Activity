n = int(input())
counter = 0


def put_queen(i, j):
    for x in range(n):
        chess_board[i][x] += 1
        chess_board[x][j] += 1
        if 0 <= i + j - x < n:
            chess_board[i + j - x][x] += 1
        if 0 <= i - j + x < n:
            chess_board[i - j + x][x] += 1
    chess_board[i][j] = -1


def remove_queen(i, j):
    for x in range(n):
        chess_board[i][x] -= 1
        chess_board[x][j] -= 1
        if 0 <= i + j - x < n:
            chess_board[i + j - x][x] -= 1
        if 0 <= i - j + x < n:
            chess_board[i - j + x][x] -= 1
    chess_board[i][j] = 0


def answer(i):
    global counter
    for j in range(n):
        if chess_board[i][j] == 0:
            put_queen(i, j)
            if i == n - 1:
                counter += 1
            else:
                answer(i + 1)
            remove_queen(i, j)


chess_board = [0] * n
for i in range(n):
    chess_board[i] = [0] * n
answer(0)
print(counter)
