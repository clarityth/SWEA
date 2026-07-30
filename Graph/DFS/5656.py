import sys
from itertools import product

sys.stdin = open("../../Implementation/sample_input (2).txt")
T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]

    def get_brick_cnt(board):
        cnt = 0
        for row in board:
            for room in row:
                if room > 0:
                    cnt += 1
        return cnt

    def boom(row, col, board):
        power = board[row][col]
        board[row][col] = 0
        cnt = 1

        for p in range(1, power):
            for i in range(4):
                nr, nc = row+p*dy[i], col+p*dx[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if board[nr][nc] > 1:
                        cnt += boom(nr, nc, board)
                        board[nr][nc] = 0
                    elif board[nr][nc] == 1:
                        board[nr][nc] = 0
                        cnt += 1
        return cnt

    def gravity(board):
        for col in range(W):
            temp = []
            for row in range(H):
                if board[row][col] > 0:
                    temp.append(board[row][col])
                board[row][col] = 0

            row = H-1
            while temp:
                board[row][col] = temp.pop()
                row -= 1

    def dfs(depth, board, remain):
        global ans

        ans = min(ans, remain)

        if depth == N or ans == 0:
            return

        for col in range(W):
            for row in range(H):
                if board[row][col] > 0:
                    next_board = [r[:] for r in board]
                    crashed = boom(row, col, next_board)
                    gravity(next_board)
                    dfs(depth+1, next_board, remain-crashed)
                    break

    ans = get_brick_cnt(board)
    dfs(0, board, ans)
    print(f"#{test_case} {ans}")