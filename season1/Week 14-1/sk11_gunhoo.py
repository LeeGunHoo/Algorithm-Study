# 일단 물음표를 > 아니면 < 로 바꿔보자

def solution(S):
    n = len(S)
    question = [i for i in range(n) if S[i] == '?']

    if not question:
        return longest_symlen(S)

def longest_symlen(S):
    n = len(S)
    max_len = 0
    for i in range(n // 2):

    return max_len

print(solution("<><??>>"))
print(solution("??????"))
print(solution("<<?"))