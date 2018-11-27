def D():
    p = 0
    r = 1
    k = 1
    for i in range(1, 1000001):
        for j in range(0, len(str(i))):
            p = p + 1
            if p == k:
                r = r * int(str(i)[j])
                k = k * 10
                print("p: %d, k: %d, r: %d" % (p, k, r))
    return r


D()
