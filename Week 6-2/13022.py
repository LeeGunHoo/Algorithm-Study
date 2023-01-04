word = input()
l = word.split("f")
s = ''


for w in l:
    for c in 'wolf':
        tmp = (len(w) // 3) * c
        s += tmp

if s == word:
    print(1)
else:
    print(0)