# import sys
from collections import deque
# sys.stdin = open("sample.txt", "r")

T = int(input())
for test_case in range(1, T+1) :
    answer = 0
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = list([[False] * (N*N) for _ in range(N)] for _ in range(N))
    q = deque()
    q.append((A, B, 0))
    visited[A][B][0] = True
    answer = -1

    # 0(o) 1(o) 2(x) 3(o) 4(o) 5(x)
    while q :
        (cur_y, cur_x, cur_time) = q.popleft()

        if (cur_y, cur_x) == (C, D) :
            answer = cur_time
            break

        for i in range(4) :
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= next_y < N and 0 <= next_x < N and not visited[next_y][next_x][cur_time+1]:
                pool_shape = grid[next_y][next_x]

                if pool_shape == 0 :  # 지나갈 수 있는 곳
                    q.append((next_y, next_x, cur_time + 1))
                    visited[next_y][next_x][cur_time+1] = True
                elif pool_shape == 2 : # 주기 2초 소용돌이
                    if cur_time % 3 == 2 : # 지나갈 수 있음
                        q.append((next_y, next_x, cur_time + 1))
                        visited[next_y][next_x][cur_time+1] = True
                    else :
                        if visited[cur_y][cur_x][cur_time+1] :
                            continue
                        visited[cur_y][cur_x][cur_time+1] = True
                        q.append((cur_y, cur_x, cur_time+1))

    print(f"#{test_case} {answer}")