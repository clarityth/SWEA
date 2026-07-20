# PRIM
import sys
import heapq
import math

sys.stdin = open("re_sample_input.txt")

T = int(input())
for test_case in range(1, T+1) :
    answer = 0
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    costs = []
    for i in range(1, N) :
        dx = xs[0] - xs[i]
        dy = ys[0] - ys[i]
        costs.append((E * (dx*dx + dy*dy), 0, i))

    heapq.heapify(costs)

    visited = set()
    visited.add(0)

    while costs :
        (cost, a, b) = heapq.heappop(costs)

        if b in visited :
            continue

        answer += cost
        visited.add(b)

        if len(visited) == N :
            break

        for i in range(N) :
            if i not in visited :
                dx = xs[b] - xs[i]
                dy = ys[b] - ys[i]
                heapq.heappush(costs,(E * (dx * dx + dy * dy), b, i))

    print(f"#{test_case} {answer}")