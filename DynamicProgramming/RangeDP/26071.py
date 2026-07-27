import sys
sys.stdin = open("../../Implementation/input_sample (1).txt")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    blocks = list(map(int, input().split()))

    if N == 1:
        print(f"#{test_case} {blocks[0]}")
        continue

    dp = [[-1] * N for _ in range(N)]

    def get_max_score(start, end):
        if start > end:
            return 0

        # DP
        if dp[start][end] != -1:
            return dp[start][end]

        max_val = -float('inf')

        # 깨트릴 블록을 탐색
        for k in range(start, end+1):
            left_val = blocks[start - 1] if start > 0 else -1 # 좌측 이웃
            right_val = blocks[end + 1] if end < N - 1 else -1 # 우측 이웃

            if left_val == -1 and right_val > 0: # 깨트릴 블록이 왼쪽 끝일 경우
                score = right_val

            elif right_val == -1 and left_val > 0: # 오른쪽 끝일 경우
                score = left_val

            elif left_val > 0 and right_val > 0: # 중간일 경우
                score = left_val * right_val

            elif left_val == -1 and right_val == -1: # 블록이 오직 하나
                score = blocks[k]

            # top-down DP
            # 좌측 구간의 최댓값 + 우측 구간의 최댓값 + 해당 블록을 깻을 때 얻는 점수
            val = get_max_score(start, k-1) + get_max_score(k+1, end) + score
            max_val = max(max_val, val)

        dp[start][end] = max_val
        return max_val

    print(f"#{test_case} {get_max_score(0, N-1)}")

