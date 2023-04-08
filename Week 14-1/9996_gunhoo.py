# 미리 패턴을 만들어 놓고, re.match를 사용해 이에 부합하는지 판단한다.
# replace를 이용해 * -> .* 로 고치고 끝에 $를 붙이면 *위치에 어떤 문자열이든 들어올 수 있고 $로 문자열 종료를 알려주게 된다.
# 다음은 쉽다. re.match는 이  정규표현식과 입력값을 대조하여 맞는 문자열인지 판단한다.

import re

n = int(input())
pattern = input().replace("*", ".*") + "$"
for _ in range(n):
    if re.match(pattern, input()):
        print("DA")
    else:
        print("NE")