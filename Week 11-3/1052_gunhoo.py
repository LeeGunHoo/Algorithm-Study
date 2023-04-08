n, k = map(int, input().split())

tmp = n

while format(tmp, 'b').count("1") > k:
    print(bin(tmp))
    tmp += 1

print(tmp - n)