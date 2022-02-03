l = [1, 2, 3, 2, 2, 3]
# l = [1, 2, 3, 2, 2, 3, 3]
# l = [1, 2, 3, 2, 2, 3, 3, 3]

d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

x = sorted(d.items(), key=lambda x: -x[1])[0][0]
print(x)
print(max(l, key=1.))