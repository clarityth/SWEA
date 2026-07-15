# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T+1) :
    answer = float('inf')
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    # print(grid)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((0, 0, 0))
    costs = [[float('inf')] * N for _ in range(N)]

    while q :
        cur_y, cur_x, cur_c = q.popleft()
        if (cur_y, cur_x) == (N-1, N-1):
            answer = min(answer, cur_c)

        if cur_c > costs[cur_y][cur_x] :
            continue

        for i in range(4):
            next_y, next_x = cur_y+dy[i], cur_x+dx[i]
            if 0 <= next_y < N and 0 <= next_x < N :
                next_c = cur_c + int(grid[next_y][next_x])

                if costs[next_y][next_x] > next_c :
                    costs[next_y][next_x] = next_c
                    q.append((next_y, next_x, next_c))

    print(f"#{test_case} {answer}")