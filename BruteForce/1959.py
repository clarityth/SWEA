# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_sum = -float('inf')

    if N > M :
        for offset in range(N-M+1):
            prod_sum = 0
            for i in range(M) :
                prod_sum += A[i+offset] * B[i]
            max_sum = max(max_sum, prod_sum)

    else :
        for offset in range(M-N+1):
            prod_sum = 0
            for i in range(N) :
                prod_sum += A[i] * B[i+offset]
            max_sum = max(max_sum, prod_sum)

    print(f"#{test_case} {max_sum}")