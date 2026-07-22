import sys

sys.stdin = open("input (6).txt")
T = 10

for test_case in range(1, T+1) :
    N = int(input())
    op = ['+', '-', '*', '/']
    answer = 1

    for i in range(N) :
        input_str = input().split()
        idx = input_str[0]
        val = input_str[1]

        if len(input_str) == 4 : # 자식 노드가 있음 -> 연산자여야함
            l_child, r_child = input_str[2], input_str[3]
            if val not in op :
                answer = 0

        else : # 리프 노드 -> 숫자여야함
            if val in op :
                answer = 0

    print(f"#{test_case} {answer}")