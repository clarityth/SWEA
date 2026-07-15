# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11) :
    test_case_num = int(input())
    answer = -1
    grid = [list(map(int, input().split())) for _ in range(100)]
    start = (99, 0)
    for i in range(100) :
        if grid[99][i] == 2 :
            start = (99, i)

    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    visited = set()

    q = deque()
    q.append(start)
    visited.add(start)
    while q :
        cur_y, cur_x = q.popleft()

        if cur_y == 0 and grid[cur_y][cur_x] == 1:
            answer = cur_x
            break

        flag = False # 좌우 이동여부 플래그
        # 좌우 먼저 탐색
        for i in range(2) :
            next_y, next_x = cur_y+dy[i], cur_x+dx[i]
            if 0 <= next_y < 100 and 0 <= next_x < 100 :
                if grid[next_y][next_x] == 1 :
                    if (next_y, next_x) not in visited :
                        q.append((next_y, next_x))
                        visited.add((next_y, next_x))
                        flag = True

        if not flag and 0 <= cur_y-1 < 100 :
            q.append((cur_y-1, cur_x))
            visited.add((cur_y-1, cur_x))

    print(f"#{test_case} {answer}")