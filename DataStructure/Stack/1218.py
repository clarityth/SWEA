# import sys
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11) :
    answer = 1
    str_len = int(input().strip())
    input_str = input().strip()

    open_par = ['(', '{', '[', '<']
    close_par = [')', '}', ']', '>']

    st = []

    for c in input_str :
        if c in open_par :
            st.append(c)

        elif c in close_par :
            if st :
                prev_open_par = st.pop()
                if not ((prev_open_par == '(' and c == ')') or (prev_open_par == '[' and c == ']') or (prev_open_par == '{' and c == '}') or ((prev_open_par == '<' and c == '>'))):
                    answer = 0
                    break
            else :
                answer = 0
                break

    if st:
        answer = 0
    print(f"#{test_case} {answer}")