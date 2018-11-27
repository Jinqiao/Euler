s = 0
for i in xrange(1, 1001):
    m = 1
    for j in xrange(0, i):
        m = (m * i) % 10000000000
    s = s + m

print(s % 10000000000)
