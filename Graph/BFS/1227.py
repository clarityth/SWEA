from collections import deque
#import sys

#sys.stdin = open("input (1).txt")

T = 10
for test_case in range(1, T+1) :
    _ = input()
    grid = list(input() for _ in range(100))
    start = (-1, -1)
    end = (-1, -1)

    for i in range(100) :
        for j in range(100) :
            if grid[i][j] == '2' :
                start = (i, j)
            if grid[i][j] == '3' :
                end = (i, j)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = set([start])
    answer = 0
    q = deque([start])

    while q :
        cur_y, cur_x = q.popleft()

        if (cur_y, cur_x) == end and grid[cur_y][cur_x] == '3':
            answer = 1
            break

        for i in range(4) :
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0 <= next_y < 100 and 0 <= next_x < 100 :
                if grid[next_y][next_x] == '0' or grid[next_y][next_x] == '3':
                    if (next_y, next_x) not in visited:
                        q.append((next_y, next_x))
                        visited.add((next_y, next_x))
    print(f"#{test_case} {answer}")