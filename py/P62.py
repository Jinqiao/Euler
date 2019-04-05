m = {}
i = 1

while True:
    i += 1
    c = i * i * i
    l = list(str(c))
    l.sort()
    k = "".join(l)
    if k in m:
        l = m[k]
        l.append(c)
        if len(l) == 5:
            for x in l:
                print(f"k: {k}, c: {x}")
            break
    else:
        m[k] = [c]
