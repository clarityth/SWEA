import sys

sys.stdin = open("input.txt")

T = int(input())

# TSP + Bit Masking
for test_case in range(1, T+1):
    N = int(input())
    pos = list(map(int, input().split()))
    company = (pos[0], pos[1])
    home = (pos[2], pos[3])
    customers = list(zip(pos[4::2], pos[5::2]))

    dp = [[float('inf')]*(1 << N) for _ in range(N)]

    # 회사 -> 첫번째 고객
    for first_customer in range(N):
        cost = abs(company[0] - customers[first_customer][0]) \
               + abs(company[1] - customers[first_customer][1])
        dp[first_customer][0] = cost

    # 고객 -> 고객
    for visited in range(1 << N):
        for current_customer in range(N):
            if dp[current_customer][visited] == float('inf'):
                continue

            for next_customer in range(N):
                if visited & (1 << next_customer):
                    continue

                next_cost = abs(customers[current_customer][0] - customers[next_customer][0]) \
                            + abs(customers[current_customer][1] - customers[next_customer][1])

                dp[next_customer][visited | (1 << next_customer)] = \
                    min(
                        dp[next_customer][visited | (1 << next_customer)],
                        dp[current_customer][visited] + next_cost
                        )

    ans = float('inf')
    # 마지막 고객 -> 집
    for final_customer in range(N):
        cost = abs(customers[final_customer][0] - home[0]) + abs(customers[final_customer][1] - home[1])
        ans = min(ans, dp[final_customer][(1 << N) - 1] + cost)

    print(f"#{test_case} {ans}")