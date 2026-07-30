import heapq
#import sys

# sys.stdin = open("input_sample (3).txt")

T = int(input())

# 0: 우, 1: 하, 2: 좌, 3: 상 (시계 방향)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    jewels = {}
    j_idx = 1
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                jewels[grid[i][j]] = (i, j)
                j_idx += 1

    # dist[(방향, 행, 열, 목표 보석 번호)] = 최소 회전 횟수
    dist = {}
    dist[(0, 0, 0, 1)] = 0

    ans = float("inf")

    # 힙 원소: (회전 횟수, 방향, 행, 열, 목표 보석 번호)
    pq = [(0, 0, 0, 0, 1)]

    while pq:
        rotate, d, row, col, target_j = heapq.heappop(pq)

        # 더 적은 회전수로 방문한 상태면 스킵
        if rotate > dist.get((d, row, col, target_j), float("inf")):
            continue

        # 보석 획득 처리
        if (row, col) == jewels.get(target_j):
            next_target = target_j + 1

            if next_target == j_idx:
                ans = rotate
                break

            # 보석 번호 증가
            if rotate < dist.get((d, row, col, next_target), float("inf")):
                dist[(d, row, col, next_target)] = rotate
                heapq.heappush(pq, (rotate, d, row, col, next_target))
            continue

        # 회전
        nd = (d + 1) % 4
        if (rotate + 1) < dist.get((nd, row, col, target_j), float("inf")):
            dist[(nd, row, col, target_j)] = rotate + 1
            heapq.heappush(pq, (rotate + 1, nd, row, col, target_j))

        # 직진 이동
        n_r, n_c = row + dy[d], col + dx[d]
        if 0 <= n_r < N and 0 <= n_c < N:
            if rotate < dist.get((d, n_r, n_c, target_j), float("inf")):
                dist[(d, n_r, n_c, target_j)] = rotate
                heapq.heappush(pq, (rotate, d, n_r, n_c, target_j))

    print(f"#{test_case} {ans}")