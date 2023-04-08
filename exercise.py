# 서로 다른 음이 아닌 정수가 적힌 n장의 숫자카드. i번째에는 a가 적혀있음.
# 카드게임을 한다. 교준이가 음이 아닌 정수 x를 알려줌. n장중 최대 k장을 선택해 제거. 남은 숫자 카드들에 대해 정수와 x를 xor한 값들의 최대값을 최소화.
# 각 x에 대해 최소화한 xor 최대값을 f(x) 라 하고 f(x)가 최소가 되는 x의 최솟값을 구해라. return : [x, f(x)]

# 테스트 케이스 :
# (n, k, a, return) = (1, 0, [7], [7, 0]) -> x가 1또는 13일 때 f(x) 최소
# (n, k, a, return) = (2, 0, [5, 9], [1, 8]) -> x가 1또는 13일 때 f(x) 최소
# (n, k, a, return) = (2, 1, [5, 9], [5, 0]) -> x가 5일 때 숫자 카드를 제거하면 최댓값이 최소가 된다.


def solution(n, k, a):
    # 정렬 후에 자른다.
    a = sorted(a, reverse=True)
    a = a[k:]
    min_xor_max = float('inf')

    # 모든 x에 대해 최댓값의 최솟값을 구한다.
    for x in range(max(a) + 1):
        xor_list = [num ^ x for num in a]
        max_xor = max(xor_list)
        min_xor_max = min(min_xor_max, max_xor)

    return [min(a), min_xor_max]

print(solution(1, 0, [7])) #[7,0]
print(solution(2, 0, [5, 9])) #[1,8]
print(solution(2, 1, [5, 9])) #[5,0]