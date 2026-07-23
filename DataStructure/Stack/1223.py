import sys
sys.stdin = open("input (7).txt")

T = 10
for test_case in range(1, T+1) :
    N = int(input())
    input_str = input()
    answer = ''
    st = []
    for c in input_str :
        if c.isdigit() :
            answer += c
        else :
            if c == '*' :
                while st and st[-1] == '*' :
                    answer += st.pop()

            elif c == '+' :
                while st and (st[-1] == '*' or st[-1] == '+') :
                    answer += st.pop()
            st.append(c)
    while st :
        answer += st.pop()

    for c in answer :
        if c.isdigit() :
            st.append(c)

        else :
            b = int(st.pop())
            a = int(st.pop())

            if c == '*' :
                st.append(a*b)
            elif c == '+' :
                st.append(a+b)

    print(f"#{test_case} {st[-1]}")
