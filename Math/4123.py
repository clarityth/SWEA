import sys
sys.stdin = open("sample_input (4).txt", "r")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    cnt = 0
    min_res = float('inf')
    max_res = -float('inf')

    def dfs(depth, temp):
        global min_res, max_res

        if depth == N:
            min_res = min(min_res, temp)
            max_res = max(max_res, temp)
            return

        for op in range(4):
            if operator[op] == 0:
                continue

            operator[op] -= 1
            num = nums[depth]

            if op == 0:
                dfs(depth + 1, temp + num)
            elif op == 1:
                dfs(depth + 1, temp - num)
            elif op == 2:
                dfs(depth + 1, temp * num)
            else:
                dfs(depth + 1, int(temp / num))

            operator[op] += 1

    dfs(1, nums[0])
    print(f"#{tc} {max_res - min_res}")