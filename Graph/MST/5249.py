from collections import defaultdict
import sys
import heapq
sys.stdin = open("sample_input.txt")

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = defaultdict(list)

    for i in range(E) :
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    ans = 0
    min_heap = []
    for (weight, node) in graph[0]:
        heapq.heappush(min_heap, (weight, node))

    visited = set([0])

    while min_heap:
        c_weight, c_node = heapq.heappop(min_heap)
        if c_node not in visited:
            ans += c_weight
            visited.add(c_node)

        else:
            continue

        if len(visited) == V+1:
            break

        for (n_weight, n_node) in graph[c_node]:
            if n_node not in visited:
                heapq.heappush(min_heap, (n_weight, n_node))

    print(f"#{test_case} {ans}")