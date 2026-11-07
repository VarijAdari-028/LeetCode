res = [0]
for b in range(n):
    res += [x | (1 << b) for x in reversed(res)]
return res