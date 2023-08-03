s = list(input())

stack = []
answer, score = 0, 1

for i in s:
    # ()
    if i == "(":
        score *= 2
        stack.append(i)
    elif i == ")":
        if stack[-1] == "[" or not stack:
            answer = 0
            break

    # []
    elif i == "[":
        stack.append(i)
        score *= 3
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break

if stack:
    print(0)
else:
    print(answer)