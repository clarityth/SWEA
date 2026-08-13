import sys
sys.stdin = open("../../../Implementation/sample_input (2).txt", "r")

T = int(input())

dr = [1, 1, -1, -1]
dc = [1, -1 ,-1, 1]

for test_case in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    def search(row, col, dir, s, start):
        global ans

        if dir == 3 and (row, col) == (start[0], start[1]):
            ans = max(ans, len(s))
            return

        if 0 <= dir < 3:
            n_row, n_col = row + dr[dir+1], col + dc[dir+1]
            if 0 <= n_row < N and 0 <= n_col < N:
                if cafes[n_row][n_col] not in s or (n_row, n_col) == start:
                    search(n_row, n_col, dir + 1, s | {cafes[n_row][n_col]}, start)  # 방향 전환

        n_row, n_col = row + dr[dir], col + dc[dir]
        if 0 <= n_row < N and 0 <= n_col < N:
            if cafes[n_row][n_col] not in s or (n_row, n_col) == start:
                search(n_row, n_col, dir, s | {cafes[n_row][n_col]}, start) # 갈 수 있을 동안 직진

    for i in range(N):
        for j in range(N):
            search(i, j, 0, set([cafes[i][j]]), (i, j))

    print(f"#{test_case} {ans}")