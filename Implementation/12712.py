# import sys
# sys.stdin = open("in1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answer = 0
    area = [list(map(int, input().split())) for _ in range(N)]

    for row in range(N) :
        for col in range(N) :
            sum_x, sum_plus = area[row][col], area[row][col]

            # +
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                for dm in range(1, M) :
                    if 0 <= row + dr*dm < N and 0 <= col + dc*dm < N :
                        sum_plus += area[row + dr*dm][col + dc*dm]

            # x
            for dr, dc in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                for dm in range(1, M):
                    if 0 <= row + dr * dm < N and 0 <= col + dc * dm < N:
                        sum_x += area[row + dr*dm][col + dc*dm]

            answer = max(answer, max(sum_plus, sum_x))

    print(f"#{test_case} {answer}")