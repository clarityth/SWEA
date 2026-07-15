# import sys
from collections import defaultdict, deque

# sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T+1) :
    length, start = map(int, input().strip().split())
    graph = defaultdict(set)
    input_data = list(map(int, input().strip().split()))

    for i in range(0, length-1, 2) :
        graph[input_data[i]].add(input_data[i+1])

    visited = set([start])
    max_time = 0
    answer = 0

    q = deque([(start, 0)])

    while q :
        cur_node, time = q.popleft()
        # print(time, answer)

        if time > max_time :
            max_time = time
            answer = cur_node

        elif time == max_time :
            answer = max(answer, cur_node)

        for next_node in graph[cur_node] :
            if next_node not in visited :
                q.append((next_node, time+1))
                visited.add(next_node)

    print(f"#{test_case} {answer}")
