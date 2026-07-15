# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11) :
    test_case_num = int(input())
    start = (1, 1)
    end = (13, 13)
    grid = [list(input()) for _ in range(16)]

    for i in range(len(grid)) :
        for j in range(len(grid[0])) :
            if grid[i][j] == '2' :
                start = (i, j)
            if grid[i][j] == '3' :
                end = (i, j)

    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    answer = 0

    while q :
        cur_y, cur_x = q.popleft()

        if (cur_y, cur_x) == end :
            answer = 1
            break

        for i in range(4) :
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= next_y < 16 and 0 <= next_x < 16 :
                if (grid[next_y][next_x] == '0' or grid[next_y][next_x] == '3') and (next_y, next_x) not in visited:
                    q.append((next_y, next_x))
                    visited.add((next_y, next_x))

    print(f"#{test_case_num} {answer}")