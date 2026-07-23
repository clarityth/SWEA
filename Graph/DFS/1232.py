import sys
sys.stdin = open("input (8).txt")

T = 10
for test_case in range(1, T+1) :
    N = int(input())
    tree = {}
    for i in range(N) :
        node_info = input().split()
        if len(node_info) == 4 : # left/right child 존재
            num, operator, l_child, r_child = int(node_info[0]), node_info[1], int(node_info[2]), int(node_info[3])
        if len(node_info) == 2 : # 리프 노드
            num, operator, l_child, r_child = int(node_info[0]), node_info[1], None, None
        tree[num] = (operator, l_child, r_child)

    def evaluate(node) :
        op, l, r = tree[node]
        if l is not None and r is not None:
            if op == '+' :
                return evaluate(l) + evaluate(r)
            elif op == '*' :
                return evaluate(l) * evaluate(r)
            elif op == '-' :
                return evaluate(l) - evaluate(r)
            else :
                return evaluate(l) / evaluate(r)

        else :
            if op.isdigit() :
                return int(op)

    print(f"#{test_case} {evaluate(1):.0f}")
