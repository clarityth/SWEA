import sys

sys.stdin = open("sample_input (1).txt")
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    input_str = input()

    rotated_nums = set()
    for i in range(N//4):
        rotate_str = (input_str[-i:]+input_str[:-i])
        for j in range(0, len(rotate_str), N // 4):
            rotated_nums.add(rotate_str[j : j+N//4])

    sorted_rotated_nums = []
    for num in rotated_nums:
        sorted_rotated_nums.append(num)
    sorted_rotated_nums.sort(reverse=True)

    def hex_to_decimal(hex):
        ans = 0
        offset = 1
        for i in range(len(hex)-1, -1, -1):
            c = hex[i]
            if c.isdigit():
                ans += int(c) * offset
            elif c.isalpha():
                ans += ((ord(c) - ord('A')) + 10) * offset
            offset *= 16
        return ans

    print(f"#{test_case} {hex_to_decimal(sorted_rotated_nums[K-1])}")