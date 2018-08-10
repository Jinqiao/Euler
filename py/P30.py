def p30(x):
    r = []
    for l in range(2, x):
        s = str(l)
        w = 0
        for i in range(0, len(s)):
            w = w + int(s[i])**5
            if w > l:
                break
        if w == l:
            r.append(w)
    return r


s = p30(1000000)
print(s)
print(sum(s))
