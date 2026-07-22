import sys
from collections import deque
sys.stdin = open("input (5).txt")
T = 10

for test_case in range(1, T+1) :
    _ = input()
    answer = 0
    grid = [list(map(int, input().split())) for _ in range(100)]
    print(grid)
    # 출발지에서 출발
    # 좌/우 먼저 탐색하고, 길 없으면 하강
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    q = deque()
    visited = [set() for _ in range(100)]

    for i in range(99, -1, -1) :
        if grid[0][i] == 1 :
            q.append((0, i, i))
            visited[i].add((0, i))

    while q :
        cur_y, cur_x, start_idx = q.popleft()
        if cur_y == 99 :
            answer = start_idx
            break

        is_moved = False
        for i in range(2) :
            next_y, next_x = cur_y+dy[i], cur_x+dx[i]

            # 1: 이동 가능
            if 0 <= next_y < 100 and 0 <= next_x < 100 and grid[next_y][next_x] == 1 and (next_y, next_x) not in visited[start_idx] :
                visited[start_idx].add((next_y, next_x))
                q.append((next_y, next_x, start_idx))
                is_moved = True

        if not is_moved :
            visited[start_idx].add((cur_y+dy[2], cur_x+dx[2]))
            q.append((cur_y+dy[2], cur_x+dx[2], start_idx))

    print(f"#{test_case} {answer}")