triangle_nums = [i * (i + 1) // 2 for i in range(45, 141)]
square_nums = [i * i for i in range(32, 100)]
pentagonal_nums = [i * (3 * i - 1) // 2 for i in range(26, 82)]
hexagonal_nums = [i * (2 * i - 1) for i in range(23, 71)]
heptagonal_nums = [i * (5 * i - 3) // 2 for i in range(21, 64)]
octagonal_nums = [i * (3 * i - 2) for i in range(19, 59)]

ts = [('squ', square_nums), ('pent', pentagonal_nums), ('hex', hexagonal_nums),
      ('hept', heptagonal_nums), ('tri', triangle_nums)]


def cyclic_nums(chain, figure):
    for mark, numbers in ts:
        if mark not in figure:
            for i in numbers:
                if str(chain[-1])[2:] == str(i)[:2]:
                    newChain = cyclic_nums(chain + [i], figure + mark)
                    if len(newChain) >= 6:
                        if str(newChain[0])[:2] == str(newChain[5])[2:]:
                            return newChain
    return chain


for num in octagonal_nums:
    result = cyclic_nums([num], 'oct')
    # print(result)
    if len(result) > 1:
        print(result)
        s = 0
        for i in result:
            s += i
        print(s)
