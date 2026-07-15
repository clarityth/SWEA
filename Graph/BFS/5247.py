# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    answer = float('inf')
    N, M = map(int, input().strip().split())

    visited = set([N])
    q = deque([(N, 0)])

    while q:
        cur_val, cur_cnt = q.popleft()

        if cur_val == M:
            answer = cur_cnt
            break

        next_vals = [cur_val * 2, cur_val - 10, cur_val - 1, cur_val + 1]

        for i in range(4):
            next_val = next_vals[i]
            if 1 <= next_val <= 1000000 and next_val not in visited:
                q.append((next_val, cur_cnt + 1))
                visited.add(next_val)

    print(f"#{test_case} {answer}")