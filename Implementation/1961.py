# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
def rotate(arr, n) :
    res = [[0] * n for _ in range(n)]
    for r in range(n) :
        for c in range(n) :
            res[c][n-r-1] = arr[r][c]
    return res

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case}")
    arr_90 = rotate(arr, N)
    arr_180 = rotate(arr_90, N)
    arr_270 = rotate(arr_180, N)

    for i in range(N):
        print(f"{''.join(map(str, arr_90[i]))} {''.join(map(str, arr_180[i]))} {''.join(map(str, arr_270[i]))}")