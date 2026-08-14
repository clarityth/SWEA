import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split()) # N: 지형 크기 X: 경사로 길이
    grid = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    def check(line):
        combo = 1

        for i in range(1, N):
            diff = line[i] - line[i - 1]

            if diff == 0:
                combo += 1

            elif diff == 1:
                if combo < X:
                    return False
                combo = 1

            elif diff == -1:
                if combo < 0:
                    return False
                combo = 1 - X

            else:
                return False

        return combo >= 0

    for row in range(N):
        if check(grid[row]):
            ans += 1

    for col in range(N):
        line = [grid[i][col] for i in range(N)]

        if check(line):
            ans += 1
    print(f"#{tc} {ans}")