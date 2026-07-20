# import sys
from collections import defaultdict

# sys.stdin = open("input.txt")
T = 10
for test_case in range(1, T+1) :
    _, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(0, len(nodes), 2) :
        a = nodes[i]
        b = nodes[i+1]
        graph[a].append(b)

    is_arrived = False
    def dfs(node, visited) :
        global is_arrived

        if node == 99 :
            is_arrived = True
            return

        if node in visited :
            return

        for next_node in graph[node] :
            dfs(next_node, visited | {node})

    dfs(0, set())
    answer = 1 if is_arrived else 0
    print(f"#{test_case} {answer}")
