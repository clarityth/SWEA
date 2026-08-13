import sys
sys.stdin = open("23667_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N: 구슬 갯수, M: 세는 칸 수, K: 반복 횟수
    nums = list(map(int, input().split()))
    nodes = {} # [id] : [prev_id, next_id, val]

    for i in range(len(nums)):
        if i == 0:
            nodes[i] = [N-1, i+1, nums[i]]
        elif i == len(nums)-1:
            nodes[i] = [i-1, 0, nums[i]]
        else:
            nodes[i] = [i-1, i+1, nums[i]]
    ins_idx = N
    tail = N-1
    work_pos = 0

    def insert_before():
        global nums, ins_idx, tail, work_pos
        right = work_pos
        for _ in range(M):
            right = nodes[right][1]

        left = nodes[right][0]
        if left == tail:
            tail = ins_idx

        nodes[right][0] = ins_idx
        nodes[left][1] = ins_idx
        nodes[ins_idx] = [left, right, nodes[left][2] + nodes[right][2]]

        work_pos = ins_idx
        ins_idx += 1

    def print_reverse():
        global tail
        ans = []
        p = tail
        for _ in range(10):
            ans.append(str(nodes[p][2]))
            p = nodes[p][0]
            if p == tail:
                break
        print(f"#{test_case}", *ans)

    for _ in range(K):
        insert_before()
    print_reverse()