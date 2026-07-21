import sys
sys.stdin = open("input.txt")

T = 10
for test_case in range(1, T+1) :
    N = int(input())
    postfix = ""
    input_str = input().strip()
    st = []
    for c in input_str :
        if c.isdigit() :
            postfix += c
        elif c in ['+', '*', '('] :
            if c == '*' :
                while st and st[-1] == '*' :
                    postfix += st.pop()
            elif c == '+' :
                while st and (st[-1] == '*' or st[-1] == '+'):
                    postfix += st.pop()
            st.append(c)

        elif c == ')' :
            while st :
                temp = st.pop()
                if temp == '(' :
                    break
                postfix += temp
    while st :
        postfix += st.pop()

    for c in postfix :
        if c in ['+', '*'] :
            b, a = int(st.pop()), int(st.pop())
            if c == '+' :
                st.append(a+b)
            else :
                st.append(a*b)
        else :
            st.append(int(c))

    print(f"#{test_case} {st[-1]}")