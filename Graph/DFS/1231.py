import sys
sys.stdin = open("input (4).txt")

T = 10
for test_case in range(1, T+1) :
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    answer = ""

    def inorder(node) :
        global answer
        idx = node-1
        if len(nodes[idx]) >= 3 :
            inorder(int(nodes[idx][2]))

        answer += nodes[idx][1]

        if len(nodes[idx]) >= 4 :
            inorder(int(nodes[idx][3]))

    inorder(1)
    print(f"#{test_case} {answer}")
