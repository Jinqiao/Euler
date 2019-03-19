import numpy as np
from itertools import permutations
from itertools import combinations


def f3(n):
    return int(n * (n + 1) / 2)


def f4(n):
    return n * n


def f5(n):
    return int(n * (3 * n - 1) / 2)


def f6(n):
    return n * (2 * n - 1)


def f7(n):
    return int(n * (5 * n - 3) / 2)


def f8(n):
    return n * (3 * n - 2)


fList = [f3, f4, f5, f6, f7, f8]
tList = []
nDict = dict()
mDict = dict()


def initDict():
    if 0 in nDict:
        return
    for i in range(0, 6):
        f = fList[i]
        nDict[i] = ls = []
        j = x = 1
        while x < 10000:
            x = f(j)
            if x >= 1000 and x < 10000 and str(x)[2] != '0' and x % 10 != 0:
                ls.append(x)
            j = j + 1


def canLink(a, b):
    return str(a)[-2:] == str(b)[:2]


def getLinkMatrices():
    for x, y in permutations(range(6), 2):
        l1 = nDict[x]
        l2 = nDict[y]
        len1 = len(l1)
        len2 = len(l2)
        m = np.full((len1, len2), False)
        for i in range(len1):
            for j in range(len2):
                m[i, j] = canLink(l1[i], l2[j])
                if m[i, j]:
                    tList.append((l1[i], l2[j]))
        mDict[(x, y)] = m


initDict()
getLinkMatrices()

# for k, v in nDict.items():
#     print(f'k: {k}, len: {len(v)}')

tSet2 = set([(t1, t2) for t1, t2 in permutations(tList, 2)
             if t1[1] == t2[0] and t1[0] != t2[1]])

tSet3 = set()
for t1, t2 in tSet2:
    for t3 in tList:
        if t2[1] == t3[0] and t1[0] != t3[1]:
            tSet3.add((t1, t2, t3))

tSet4 = set()
for t1, t2, t3 in tSet3:
    for t4 in tList:
        if t3[1] == t4[0] and t1[0] != t4[1]:
            tSet4.add((t1, t2, t3, t4))

tSet5 = set()
for t1, t2, t3, t4 in tSet4:
    for t5 in tList:
        if t4[1] == t5[0] and t1[0] != t5[1]:
            tSet5.add((t1, t2, t3, t4, t5))

tSet6 = set()
for t1, t2, t3, t4, t5 in tSet5:
    for t6 in tList:
        if t5[1] == t6[0] and t1[0] == t6[1]:
            tSet6.add((t1, t2, t3, t4, t5, t6))

seqList = []
for a in tSet6:
    seqList.append([t[0] for t in a])

seqDict = {}
for seq in seqList:
    seq2 = seq.copy()
    seq2.sort()
    k = tuple(seq2)
    if k not in seqDict:
        seqDict[k] = seq

seqDict2 = {}
for seqK, seq in seqDict.items():
    L = []
    for n in seq:
        S = set()
        for i, l in nDict.items():
            if n in l:
                S.add(i)
        L.append(list(S))
    L2 = sum(L, [])
    S2 = set(L2)
    if len(S2) == 6 and len([(l1, l2) for (l1, l2) in combinations(L, 2)
                             if l1 == l2]) == 0:
        seqDict2[seqK] = L

print(sum(list(seqDict2.keys())[0]))
